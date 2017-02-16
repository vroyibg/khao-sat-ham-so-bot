import sympy
from matplotlib import pyplot
import matplotlib as mpl
from dao_ham import *
from tap_xac_dinh import *
from xu_ly_chuoi import *
from gioi_han import *


def ve_bang_bien_thien(ham_so, bien, ten_file):
    # Tinh toan cac gia tri can thiet
    dao_ham_cap_1 = sympy.simplify(sympy.diff(ham_so, bien))
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    dao_ham_cap_1_kxd = khong_xac_dinh(dao_ham_cap_1, bien)
    ham_so_kxd = khong_xac_dinh(ham_so, bien)
    cac_gia_tri_can_dien_vao_x = list(
        set(nghiem_dao_ham_cap_1 + dao_ham_cap_1_kxd + ham_so_kxd))
    cac_gia_tri_can_dien_vao_x.sort()
    cac_gia_tri_can_dien_vao_x = [-sympy.oo] + \
        cac_gia_tri_can_dien_vao_x + [sympy.oo]

    # Tinh chinh bang
    mpl.rc("text", usetex=True)
    fig = pyplot.figure()
    bang_bien_thien = fig.add_subplot(111)
    bang_bien_thien.xaxis.set_visible(False)
    bang_bien_thien.yaxis.set_visible(False)
    co_font = 20
    chieu_rong_cot_ngan = co_font * 2
    chieu_rong_bang = 800
    chieu_cao_bang = 200
    pyplot.gca().set_aspect('equal', adjustable='box')

    # Ve khung cua bang bien thien
    bang_bien_thien.plot([0, chieu_rong_bang], [
                         chieu_cao_bang / 5 * 4, chieu_cao_bang / 5 * 4], 'k-', lw=2)
    bang_bien_thien.plot([0, chieu_rong_bang], [
                         chieu_cao_bang / 5 * 3, chieu_cao_bang / 5 * 3], 'k-', lw=2)
    bang_bien_thien.plot([chieu_rong_cot_ngan, chieu_rong_cot_ngan], [
                         0, chieu_cao_bang], 'k-', lw=2)
    mpl.rcParams.update(
        {'font.size': co_font * (fig.get_size_inches()[1] * fig.dpi) / chieu_rong_bang})
    bang_bien_thien.text(chieu_rong_cot_ngan / 2, chieu_cao_bang / 5 * 4.5,
                         r"$x$", verticalalignment='center', horizontalalignment='center')
    bang_bien_thien.text(chieu_rong_cot_ngan / 2, chieu_cao_bang /
                         5 * 3.5, r"$y'$", verticalalignment='center', horizontalalignment='center')
    bang_bien_thien.text(chieu_rong_cot_ngan / 2, chieu_cao_bang /
                         5 * 1.5, r"$y$", verticalalignment='center', horizontalalignment='center')

    # Tinh khoang cach giua cac gia tri
    phong_hai_dau = co_font * 2
    khoang_cach = int((chieu_rong_bang - chieu_rong_cot_ngan -
                       phong_hai_dau * 2) / (len(cac_gia_tri_can_dien_vao_x) - 1))

    # Dien vao hang x va hang y'
    for i in range(len(cac_gia_tri_can_dien_vao_x)):
        bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i, chieu_cao_bang / 5 * 4.5,
                             boc_latex_mpl(cac_gia_tri_can_dien_vao_x[i]), verticalalignment='center', horizontalalignment='center')
        if i != 0 and i != len(cac_gia_tri_can_dien_vao_x) - 1:
            if cac_gia_tri_can_dien_vao_x[i] in dao_ham_cap_1_kxd:
                bang_bien_thien.plot([chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i - 2, chieu_rong_cot_ngan + phong_hai_dau +
                                      khoang_cach * i - 2], [chieu_cao_bang / 5 * 4, chieu_cao_bang / 5 * 3])
                bang_bien_thien.plot([chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + 2, chieu_rong_cot_ngan + phong_hai_dau +
                                      khoang_cach * i + 2], [chieu_cao_bang / 5 * 4, chieu_cao_bang / 5 * 3])
            else:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i, chieu_cao_bang /
                                     5 * 3.5, boc_latex_mpl("0"), verticalalignment='center', horizontalalignment='center')

    # Gioi han cua ham so tai vo cuc
    gioi_han_vo_cuc = tim_gioi_han_tai_vo_cuc(ham_so, bien)
    # Cac gia tri cua y can dien vao bang
    gia_tri_ham_so = []
    for gia_tri in cac_gia_tri_can_dien_vao_x:

        # Neu ham so khong xac dinh thi tim gioi han hai phia
        if gia_tri in ham_so_kxd:
            gia_tri_ham_so.append(tim_gioi_han_hai_phia(ham_so, bien, gia_tri))

        # Neu khong thi tim gia tri
        else:
            if gia_tri == -sympy.oo:
                gia_tri_ham_so.append(gioi_han_vo_cuc[0])
            elif gia_tri == sympy.oo:
                gia_tri_ham_so.append(gioi_han_vo_cuc[1])
            else:
                gia_tri_ham_so.append(ham_so.subs(bien, gia_tri))

    phong_kxd = co_font * 1.5
    # Dien vao dong y
    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            if isinstance(gia_tri_ham_so[i - 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i - 1][1]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i - 1]
            if gia_tri_ham_so[i][0] > gia_tri_so_sanh:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i - phong_kxd, chieu_cao_bang /
                                     5 * 2.5, boc_latex_mpl(gia_tri_ham_so[i][0]), verticalalignment='center', horizontalalignment='center')
            else:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i - phong_kxd, chieu_cao_bang /
                                     5 * 0.5, boc_latex_mpl(gia_tri_ham_so[i][0]), verticalalignment='center', horizontalalignment='center')
            if isinstance(gia_tri_ham_so[i + 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i + 1]
            if gia_tri_ham_so[i][1] > gia_tri_so_sanh:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + phong_kxd, chieu_cao_bang /
                                     5 * 2.5, boc_latex_mpl(gia_tri_ham_so[i][1]), verticalalignment='center', horizontalalignment='center')
            else:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + phong_kxd, chieu_cao_bang /
                                     5 * 0.5, boc_latex_mpl(gia_tri_ham_so[i][1]), verticalalignment='center', horizontalalignment='center')
        else:
            if isinstance(gia_tri_ham_so[i + 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i + 1]
            if gia_tri_ham_so[i] < gia_tri_so_sanh:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i, chieu_cao_bang / 5 *
                                     0.5, boc_latex_mpl(gia_tri_ham_so[i]), verticalalignment='center', horizontalalignment='center')
            else:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i, chieu_cao_bang / 5 *
                                     2.5, boc_latex_mpl(gia_tri_ham_so[i]), verticalalignment='center', horizontalalignment='center')

    # Dien cac dau + va - vao dong y'
    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            gia_tri = gia_tri_ham_so[i][1]
        else:
            gia_tri = gia_tri_ham_so[i]
        if isinstance(gia_tri_ham_so[i + 1], tuple):
            gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
        else:
            gia_tri_so_sanh = gia_tri_ham_so[i + 1]

        if gia_tri < gia_tri_so_sanh:
            bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (i + 0.5), chieu_cao_bang /
                                 5 * 3.5, boc_latex_mpl("+"), verticalalignment='center', horizontalalignment='center')
        else:
            bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (i + 0.5), chieu_cao_bang /
                                 5 * 3.5, boc_latex_mpl("-"), verticalalignment='center', horizontalalignment='center')

    # Ve cac mui ten len xuong
    cong_them = phong_kxd

    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            gia_tri = gia_tri_ham_so[i][1]
            bang_bien_thien.plot([chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i - 2, chieu_rong_cot_ngan + phong_hai_dau +
                                  khoang_cach * i - 2], [chieu_cao_bang / 5 * 3, 0])
            bang_bien_thien.plot([chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + 2, chieu_rong_cot_ngan + phong_hai_dau +
                                  khoang_cach * i + 2], [chieu_cao_bang / 5 * 3, 0])
            # draw.line((chieu_rong_cot_ngan + khoang_cach * i - 2, chieu_cao_bang / 5 * 2, chieu_rong_cot_ngan +
            #           khoang_cach * i - 2, chieu_cao_bang - 1), fill=mau_but)
            # draw.line((chieu_rong_cot_ngan + khoang_cach * i + 2, chieu_cao_bang / 5 * 2, chieu_rong_cot_ngan +
            #           khoang_cach * i + 2, chieu_cao_bang - 1), fill=mau_but)
        else:
            gia_tri = gia_tri_ham_so[i]
        if isinstance(gia_tri_ham_so[i + 1], tuple):
            gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
        else:
            gia_tri_so_sanh = gia_tri_ham_so[i + 1]
        if isinstance(gia_tri_ham_so[i], tuple):
            x1 = chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + phong_kxd * 2
        else:
            x1 = chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + phong_kxd

        if isinstance(gia_tri_ham_so[i + 1], tuple):
            x2 = chieu_rong_cot_ngan + phong_hai_dau + \
                khoang_cach * (i + 1) - phong_kxd * 2
        else:
            x2 = chieu_rong_cot_ngan + phong_hai_dau + \
                khoang_cach * (i + 1) - phong_kxd

        if gia_tri < gia_tri_so_sanh:
            bang_bien_thien.arrow(x1, chieu_cao_bang / 5, x2 - x1, chieu_cao_bang /
                                  5, head_width=co_font / 3, head_length=co_font / 2)
        else:
            bang_bien_thien.arrow(x1, chieu_cao_bang / 5 * 2, x2 - x1, -
                                  chieu_cao_bang / 5, head_width=co_font / 3, head_length=co_font / 2)
    # Dien gia tri y cuoi cung ( gia tri cua y o duong vo cung)
    if isinstance(gia_tri_ham_so[-2], tuple):
        gia_tri_so_sanh = gia_tri_ham_so[-2][1]
    else:
        gia_tri_so_sanh = gia_tri_ham_so[-2]
    if gia_tri_ham_so[-1] < gia_tri_so_sanh:
        bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (len(cac_gia_tri_can_dien_vao_x) - 1),
                             chieu_cao_bang / 5 * 0.5, boc_latex_mpl(gia_tri_ham_so[-1]), verticalalignment='center', horizontalalignment='center')
    else:
        bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (len(cac_gia_tri_can_dien_vao_x) - 1),
                             chieu_cao_bang / 5 * 2.5, boc_latex_mpl(gia_tri_ham_so[-1]), verticalalignment='center', horizontalalignment='center')
    fig.savefig(ten_file, bbox_inches='tight', pad_inches=0.0)
    pyplot.close(fig)



# Ve bang su dung thu vien xu ly anh PIL ->>> Rat cham
# Chi de phong truong hop matplotlib khong dung duoc

def ve_bang_bien_thien1(ham_so, bien, ten_file):
    #n= time.time()
    dao_ham_cap_1 = sympy.diff(ham_so, bien)
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    dao_ham_cap_1_kxd = khong_xac_dinh(dao_ham_cap_1, bien)
    ham_so_kxd = khong_xac_dinh(ham_so, bien)
    cac_gia_tri_can_dien_vao_x = list(
        set(nghiem_dao_ham_cap_1 + dao_ham_cap_1_kxd + ham_so_kxd))
    cac_gia_tri_can_dien_vao_x.sort()
    cac_gia_tri_can_dien_vao_x = [-sympy.oo] + \
        cac_gia_tri_can_dien_vao_x + [sympy.oo]
    # print(time.time()-n)
    #n = time.time()
    # Ve khung cua bang bien thien
    co_font = 20
    chieu_rong_cot_ngan = co_font * 2
    chieu_rong_bang = 600
    chieu_cao_bang = 200
    mau_but = 0

    fnt = ImageFont.truetype("./arial.ttf", co_font)
    bang_bien_thien = Image.new(
        "RGB", (chieu_rong_bang, chieu_cao_bang), "white")
    draw = ImageDraw.Draw(bang_bien_thien)
    draw.line((0, chieu_cao_bang / 5, chieu_rong_bang -
               1, chieu_cao_bang / 5), fill=mau_but)
    draw.line((0, chieu_cao_bang / 5 * 2, chieu_rong_bang -
               1, chieu_cao_bang / 5 * 2), fill=mau_but)
    draw.line((chieu_rong_cot_ngan, 0, chieu_rong_cot_ngan,
               chieu_cao_bang - 1), fill=mau_but)
    draw.text((co_font / 2, co_font / 2), 'x', fill=mau_but, font=fnt)
    draw.text((co_font / 2, co_font / 2 + chieu_cao_bang / 5),
              'y', fill=mau_but, font=fnt)
    draw.text((co_font / 2, co_font / 2 + chieu_cao_bang / 5 * 4),
              "y'", fill=mau_but, font=fnt)
    khoang_cach = int((chieu_rong_bang - chieu_rong_cot_ngan -
                       co_font) / (len(cac_gia_tri_can_dien_vao_x) - 1))
    #print(time.time() - n)
    #n = time.time()

    # Dien vao hang x va hang y'
    for i in range(len(cac_gia_tri_can_dien_vao_x)):
        anh_cua_bieu_thuc = ve_bieu_thuc_toan_ra_anh(
            cac_gia_tri_can_dien_vao_x[i])
        bang_bien_thien.paste(anh_cua_bieu_thuc, (int(
            chieu_rong_cot_ngan + khoang_cach * i), int(co_font / 2)))
        if i != 0 and i != len(cac_gia_tri_can_dien_vao_x) - 1:
            if cac_gia_tri_can_dien_vao_x[i] in dao_ham_cap_1_kxd:
                draw.line((chieu_rong_cot_ngan + khoang_cach * i - 2, chieu_cao_bang / 5, chieu_rong_cot_ngan +
                           khoang_cach * i - 2, chieu_cao_bang / 5 * 2), fill=mau_but)
                draw.line((chieu_rong_cot_ngan + khoang_cach * i + 2, chieu_cao_bang / 5, chieu_rong_cot_ngan +
                           khoang_cach * i + 2, chieu_cao_bang / 5 * 2), fill=mau_but)
            else:
                draw.text((chieu_rong_cot_ngan + khoang_cach * i, co_font / 2 + chieu_cao_bang / 5),
                          str(0), fill=mau_but, font=fnt)

    #print(time.time() - n)
    #n = time.time()
    # Gioi han cua ham so tai vo cuc
    gioi_han_vo_cuc = tim_gioi_han_tai_vo_cuc(ham_so, bien)
    # Cac gia tri cua y can dien vao bang
    gia_tri_ham_so = []
    for gia_tri in cac_gia_tri_can_dien_vao_x:

        # Neu ham so khong xac dinh thi tim gioi han hai phia
        if gia_tri in ham_so_kxd:
            gia_tri_ham_so.append(tim_gioi_han_hai_phia(ham_so, bien, gia_tri))

        # Neu khong thi tim gia tri
        else:
            if gia_tri == -sympy.oo:
                gia_tri_ham_so.append(gioi_han_vo_cuc[0])
            elif gia_tri == sympy.oo:
                gia_tri_ham_so.append(gioi_han_vo_cuc[1])
            else:
                gia_tri_ham_so.append(ham_so.subs(bien, gia_tri))

    #print(time.time() - n)
    #n = time.time()
    # Dien vao dong y
    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            if isinstance(gia_tri_ham_so[i - 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i - 1][1]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i - 1]
            if gia_tri_ham_so[i][0] > gia_tri_so_sanh:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i][0]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i - co_font * 1.5), int(co_font / 2 + chieu_cao_bang / 5 * 2)))
            else:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i][0]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i - co_font * 1.5), int(co_font / 2 + chieu_cao_bang / 5 * 4)))
            if isinstance(gia_tri_ham_so[i + 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i + 1]
            if gia_tri_ham_so[i][1] > gia_tri_so_sanh:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i][1]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i + co_font / 2), int(co_font / 2 + chieu_cao_bang / 5 * 2)))
            else:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i][1]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i + co_font / 2), int(co_font / 2 + chieu_cao_bang / 5 * 4)))
        else:
            if isinstance(gia_tri_ham_so[i + 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i + 1]
            if gia_tri_ham_so[i] < gia_tri_so_sanh:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i), int(co_font / 2 + chieu_cao_bang / 5 * 4)))
            else:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i), int(co_font / 2 + chieu_cao_bang / 5 * 2)))

    #print(time.time() - n)
    #n = time.time()
    # Dien cac dau + va - vao dong y'
    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            gia_tri = gia_tri_ham_so[i][1]
        else:
            gia_tri = gia_tri_ham_so[i]
        if isinstance(gia_tri_ham_so[i + 1], tuple):
            gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
        else:
            gia_tri_so_sanh = gia_tri_ham_so[i + 1]

        if gia_tri < gia_tri_so_sanh:
            draw.text((chieu_rong_cot_ngan + khoang_cach * (i + 1 / 2), co_font / 2 + chieu_cao_bang / 5),
                      "+", fill=mau_but, font=fnt)
        else:
            draw.text((chieu_rong_cot_ngan + khoang_cach * (i + 1 / 2), co_font / 2 + chieu_cao_bang / 5),
                      "-", fill=mau_but, font=fnt)

    #print(time.time() - n)
    #n = time.time()
    # Ve cac mui ten len xuong
    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            gia_tri = gia_tri_ham_so[i][1]
            draw.line((chieu_rong_cot_ngan + khoang_cach * i - 2, chieu_cao_bang / 5 * 2, chieu_rong_cot_ngan +
                       khoang_cach * i - 2, chieu_cao_bang - 1), fill=mau_but)
            draw.line((chieu_rong_cot_ngan + khoang_cach * i + 2, chieu_cao_bang / 5 * 2, chieu_rong_cot_ngan +
                       khoang_cach * i + 2, chieu_cao_bang - 1), fill=mau_but)
        else:
            gia_tri = gia_tri_ham_so[i]
        if isinstance(gia_tri_ham_so[i + 1], tuple):
            gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
        else:
            gia_tri_so_sanh = gia_tri_ham_so[i + 1]
        if isinstance(gia_tri_ham_so[i], tuple):
            x1 = chieu_rong_cot_ngan + khoang_cach * i + co_font * 1.5
        else:
            x1 = chieu_rong_cot_ngan + khoang_cach * i + co_font

        if isinstance(gia_tri_ham_so[i + 1], tuple):
            x2 = chieu_rong_cot_ngan + khoang_cach * (i + 1) - co_font * 1.5
        else:
            x2 = chieu_rong_cot_ngan + khoang_cach * (i + 1)

        if gia_tri < gia_tri_so_sanh:
            draw.line((x1, co_font / 2 + chieu_cao_bang / 5 * 4, x2,
                       co_font / 2 + chieu_cao_bang / 5 * 2 + co_font), fill=mau_but)
        else:
            draw.line((x1, co_font / 2 + chieu_cao_bang / 5 * 2 + co_font,
                       x2, co_font / 2 + chieu_cao_bang / 5 * 4), fill=mau_but)
    #print(time.time() - n)
    #n = time.time()
    # Dien gia tri y cuoi cung ( gia tri cua y o duong vo cung)
    if isinstance(gia_tri_ham_so[-2], tuple):
        gia_tri_so_sanh = gia_tri_ham_so[-2][1]
    else:
        gia_tri_so_sanh = gia_tri_ham_so[-2]
    if gia_tri_ham_so[-1] < gia_tri_so_sanh:
        bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[-1]), (int(
            chieu_rong_cot_ngan + khoang_cach * (len(cac_gia_tri_can_dien_vao_x) - 1)), int(co_font / 2 + chieu_cao_bang / 5 * 4)))
    else:
        bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[-1]), (int(
            chieu_rong_cot_ngan + khoang_cach * (len(cac_gia_tri_can_dien_vao_x) - 1)), int(co_font / 2 + chieu_cao_bang / 5 * 2)))
    bang_bien_thien.save(ten_file)
