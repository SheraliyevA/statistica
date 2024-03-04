from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import permissions
from django.db.models import Sum
class XodimDetail(APIView):
    parser_classes = [JSONParser, MultiPartParser]
    def get(self, request, id):
        try:
            xodim = Xodim.objects.get(id=id)
            ser = XodimSerializer(xodim)
            l=[]
            s=[]
            m=[]
            h = Hisobot.objects.filter(xodim=xodim)
            sum_xato = h.aggregate(soni=Sum('xato_soni'))
            sum_butun = h.aggregate(soni=Sum('butun_soni'))
            ish_vaqti=h.aggregate(umumiy_ish_vaqti=Sum('ish_vaqti'))
            s.append({
            'id': xodim.id,
            'xodimi': xodim.first_name,
            'Jami_xato': sum_xato,
            'Jami_butun': sum_butun,
            'Ish_vaqti_soat':ish_vaqti
            })
        
            d={}
            for j in h:
                a = j.mahsulot.name
                xodim_mistakes = Hisobot.objects.filter(xodim=j.xodim, mahsulot=j.mahsulot)
                xodim_mistakes_aggregated = xodim_mistakes.aggregate(total_xato_soni=Sum('xato_soni'))
                d[str(j.mahsulot.name)] = xodim_mistakes_aggregated['total_xato_soni']


            for j in h:
                l.append({
                'mahsulot_name': j.mahsulot.name,
                'xato_soni': j.xato_soni,
                'butun_soni': j.butun_soni,
            })
            return Response({'foydalanuchi haqida malumot':ser.data,
                                'barcha_statistica': s,
                                'mahsulot_xato_soni':d,
                                'statistica':l,
                                })
        except:
            return Response({'error': "Xato id kiritildi"})

    def patch(self, request, id):
        a = request.data.getlist('ish_turi', [])
        xodim = Xodim.objects.get(id=id)
        serializers = XodimSerializer(xodim, data = request.data, partial=True)
        if serializers.is_valid():
            s = serializers.save()
            if a:
                s.ish_turi.clear()
                for x in a:
                    s.ish_turi.add(x)
            return Response(serializers.data)
        return Response(serializers.errors)

    def delete(self, request, id):
        xodim = Xodim.objects.get(id=id).delete()
        return Response({'message':' {} xodim o\'chirildi'.format(xodim[0])})

    


class XodimMahsulotStat(APIView):
    def get(self, request, *args, **kwargs):
        xodimlar = Xodim.objects.all()
        error="Mahsulot bo'yicha xatolar"
        xodimlar_stat = []

        for xodim in xodimlar:
            mahsulotlar = Maxsulot.objects.all()
            xodimish=Hisobot.objects.all()
            if xodimish:
                vaqti=[obj.ish_vaqti for obj in xodimish]
                j_vaqti = sum(vaqti)     

                xatolar1=[obj.butun_soni for obj in xodimish]
                all_stat = sum(xatolar1)
                mini = min(xatolar1)
                maks=max(xatolar1)
                xato_stat=[obj.xato_soni for obj in xodimish]

                all_stat1=sum(xato_stat)
                max_stat=max(xato_stat)
                min_stat=min(xato_stat)
                errorr="Butun mahsulotlar"
                xodim_stat = {
                    'xodim_id': xodim.id,
                    'xodim':xodim.first_name.title(),
                    "mahsulot":errorr,
                    'barcha_xatolar':all_stat,
                    'maksimum_xatolar':max_stat,
                    'minimum_xatolar':min_stat,


                    'mahsulot':error,
                    'butun_maxsulotlar_jami':all_stat,
                    'butun_minsulotlar_minimum': mini,
                    'butun_mahsulotlar_maksimum':maks,                    
                    'Ish_vaqti_soat':vaqti,
                    'jami_soat':j_vaqti,

                    'mahsulotlar':[mahsulot.name for mahsulot in mahsulotlar]

                }
                
                xodimlar_stat.append(xodim_stat)

        return Response(xodimlar_stat)
    
# class XodimStat(APIView):
#     def get(self, request, xodim_id, *args, **kwargs):
#         try:
#             xodim = Xodim.objects.get(id=xodim_id)
#             mahsulotlar = Mahsulot.objects.all()
            
#             if mahsulotlar:
#                 xatolar = [mahsulot.xato_soni for mahsulot in mahsulotlar]
#                 maksimal = max(xatolar)
#                 minimal = min(xatolar)
#                 ortacha = sum(xatolar)/len(xatolar)
                
#                 xodim_stat = {
#                     'xodim_id': xodim.id,
#                     'maksimal': maksimal,
#                     'minimal': minimal,
#                     'o\'rtacha': ortacha,
#                     'mahsulotlar':[mahsulot.nomi for mahsulot in mahsulotlar]
#                 }
                
#                 return Response(xodim_stat)
#             else:
#                 return Response({'message': 'Xodimning mahsuloti yo\'q'})
#         except Xodim.DoesNotExist:
#             return Response({'message': 'Xodim topilmadi'})
