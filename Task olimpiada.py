# # Bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. Biz isə onların topladığı xallara
#  görə neçənci yeri tutduğunu print etməliyik. Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
# # Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
# # Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş sıraya uyğun sıralanacaq və nəticə
#   düzgün olmayacaq. (taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)
# # Verilmiş xallara uyğun tutduğu yerləri gətirən bir funksiya yazın.

points=[9,3,1,4,5,7,8,6,2]
def sirala():
    place=1
    for i in points:
        for j in range(len(points)):
            if i < points[j]:
                place+=1
        print(f"{place}-ci yer")
        place=1
sirala()
