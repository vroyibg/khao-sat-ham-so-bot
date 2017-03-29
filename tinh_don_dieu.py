import dao_ham
import tinh_xac_dinh
import xu_ly_chuoi
import bat_dang_thuc
import phuong_trinh
import sympy
import phuong_trinh_bac_2
import huong_dan_giai
import hang_so


def tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh(ham_so, bien, tham_so):
    # De bai
    loi_giai = huong_dan_giai.LoiGiai("Tìm {0} để hàm số {1} đồng biến trên tập xác định".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax("f({0})={1}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so)))))

    # Buoc 1 tim tap xac dinh
    buoc_1 = huong_dan_giai.LoiGiai("Tìm tập xác định của hàm số")

    tap_xac_dinh = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax("D=" + xu_ly_chuoi.tao_latex(tap_xac_dinh)))

    buoc_1.dap_an = tap_xac_dinh

    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 tim dao ham
    buoc_2 = huong_dan_giai.LoiGiai("Tìm đạo hàm của hàm số")

    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(
        "f'({0})={1}".format(bien, xu_ly_chuoi.tao_latex(dao_ham_cap_1))))

    dao_ham_cap_1_rut_gon = phuong_trinh.rut_gon(dao_ham_cap_1)
    if dao_ham_cap_1_rut_gon != dao_ham_cap_1:
        buoc_2.them_thao_tac(
            xu_ly_chuoi.boc_mathjax("\Leftrightarrow " + xu_ly_chuoi.tao_latex(dao_ham_cap_1)))
    # buoc_2.them_thao_tac("Để hàm số đồng biến trên D thì " +
    #                xu_ly_chuoi.boc_mathjax(
    #                   "f'(x)\geq0,\\forall " + xu_ly_chuoi.tao_latex(bien) + " \in D"))
    buoc_2.dap_an = dao_ham_cap_1_rut_gon
    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3 tim tham so de dao ham lon hon hoac bang 0 tren R
    buoc_3 = phuong_trinh_bac_2.tim_tham_so_de_ham_so_lon_hon_hoac_bang_0(dao_ham_cap_1_rut_gon, bien, tham_so)
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.dap_an = buoc_3.dap_an

    return loi_giai


def tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh(ham_so, bien, tham_so):
    # De bai
    loi_giai = huong_dan_giai.LoiGiai("Tìm {0} để hàm số {1} nghịch biến trên tập xác định".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax("f({0})={1}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so)))))

    # Buoc 1 tim tap xac dinh
    buoc_1 = huong_dan_giai.LoiGiai("Tìm tập xác định của hàm số")

    tap_xac_dinh = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax("D=" + xu_ly_chuoi.tao_latex(tap_xac_dinh)))

    buoc_1.dap_an = tap_xac_dinh

    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 tim dao ham
    buoc_2 = huong_dan_giai.LoiGiai("Tìm đạo hàm của hàm số")

    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(
        "f'({0})={1}".format(bien, xu_ly_chuoi.tao_latex(dao_ham_cap_1))))

    dao_ham_cap_1_rut_gon = phuong_trinh.rut_gon(dao_ham_cap_1)
    if dao_ham_cap_1_rut_gon != dao_ham_cap_1:
        buoc_2.them_thao_tac(
            xu_ly_chuoi.boc_mathjax("\Leftrightarrow " + xu_ly_chuoi.tao_latex(dao_ham_cap_1)))

    # buoc_2.them_thao_tac("Để hàm số đồng biến trên D thì " +
    #                xu_ly_chuoi.boc_mathjax(
    #                   "f'(x)\geq0,\\forall " + xu_ly_chuoi.tao_latex(bien) + " \in D"))

    buoc_2.dap_an = dao_ham_cap_1_rut_gon
    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3 tim tham so de dao ham lon hon hoac bang 0 tren R
    buoc_3 = phuong_trinh_bac_2.tim_tham_so_de_ham_so_nho_hon_hoac_bang_0(dao_ham_cap_1_rut_gon, bien, tham_so)
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.dap_an = buoc_3.dap_an

    return loi_giai


def tim_tham_so_de_ham_so_don_tren_1_khoang_co_do_dai_k(ham_so, bien, tham_so, do_dai_khoang):
    # De bai
    loi_giai = huong_dan_giai.LoiGiai("Tìm {0} để hàm số {1} đơn điệu trên khoảng có độ dài {do_dai}".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax("f({0})={1}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so))),
        do_dai=str(do_dai_khoang)))

    # Buoc 1 : Tim dao ham
    buoc_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm đạo hàm của hàm số'

    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 : Tim tham so de f' co 2 nghiem phan biet va quan he nghiem
    buoc_2 = huong_dan_giai.LoiGiai('Tìm {ts} để đạo hàm có 2 nghiệm phân biệt và quan hệ giữa 2 nghiệm'.format(
        ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))

    # Buoc 2.1: Tim tham so de f' co 2 nghiem phan biet
    buoc_2_1 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(buoc_1.dap_an, bien, tham_so)
    del buoc_2_1.cac_buoc_giai[2]
    buoc_2_1.ten_loi_giai = 'Tìm {ts} để đạo hàm có 2 nghiệm phân biệt'.format(
        ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)))

    buoc_2.them_thao_tac(buoc_2_1)
    # buoc 2.2: Tim quan he giua hai nghiem
    buoc_2_2 = phuong_trinh_bac_2.quan_he_2_nghiem_viet(buoc_1.dap_an, bien)
    buoc_2_2.ten_loi_giai = 'Áp dụng định lý Viet tìm quan hệ giữa hai nghiệm của đạo hàm'

    buoc_2.them_thao_tac(buoc_2_2)

    loi_giai.them_thao_tac(buoc_2)

    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')
    # buoc 3: phan tich dieu kien thanh dang viet
    buoc_3 = huong_dan_giai.LoiGiai('Phân tích điều kiện và đưa về dạng Vi-et')
    dieu_kien = bat_dang_thuc.bang(sympy.Abs(nghiem_1 - nghiem_2), do_dai_khoang)
    buoc_3.them_thao_tac('Để hàm số đơn điệu trên khoảng có độ dài {do_dai} thì {dk}'.format(
        do_dai=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(do_dai_khoang)),
        dk=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien))))

    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))
    dieu_kien = bat_dang_thuc.bang((nghiem_1 + nghiem_2) ** 2 - 4 * nghiem_1 * nghiem_2, do_dai_khoang ** 2)

    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))
    # chuyen ve
    dieu_kien = bat_dang_thuc.bang(dieu_kien.lhs - dieu_kien.rhs, 0)
    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    buoc_3.dap_an = dieu_kien.lhs
    loi_giai.them_thao_tac(buoc_3)

    # Buoc 4: The nghiem,giai phuong trinh tim nghiem
    buoc_4 = huong_dan_giai.LoiGiai('Thế kết quả từ bước 2 vào bước 3 và giải phương trình tìm nghiệm')
    buoc_4.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))
    buoc_4.them_thao_tac('Thế kết quả từ bước 2 ta được:')
    # The bien
    dieu_kien = phuong_trinh.the_bieu_thuc(dieu_kien, nghiem_1 + nghiem_2, buoc_2_2.dap_an[0])
    dieu_kien = phuong_trinh.the_bieu_thuc(dieu_kien, nghiem_1 * nghiem_2, buoc_2_2.dap_an[1])
    # buoc_4.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    loi_giai_phuong_trinh = phuong_trinh.giai_phuong_trinh(dieu_kien.lhs, tham_so)
    buoc_4.cac_buoc_giai += loi_giai_phuong_trinh.cac_buoc_giai

    buoc_4.dap_an=loi_giai_phuong_trinh.dap_an
    loi_giai.them_thao_tac(buoc_4)

    # buoc 5 : tong hop ket qua
    buoc_5 = huong_dan_giai.LoiGiai('Tổng hợp kết quả')
    buoc_5.them_thao_tac('Tổng hợp kết quả ta được:')
    thoa_man = []
    for nghiem in buoc_4.dap_an:
        if buoc_2_1.dap_an.contains(nghiem):
            thoa_man.append(nghiem)

    if thoa_man==[]:
        buoc_5.them_thao_tac('Không có {ts} nào thỏa mãn điều kiện đề bài'.format(ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))
    else:
        buoc_5.them_thao_tac('Với {ts} thì thỏa mãn'.format(ts=xu_ly_chuoi.boc_mathjax('{tham_so}={nghiem}'.format(tham_so=xu_ly_chuoi.tao_latex(tham_so),nghiem=xu_ly_chuoi.tao_ngoac_nhon(thoa_man)))))

    buoc_5.dap_an=thoa_man
    loi_giai.them_thao_tac(buoc_5)

    return loi_giai


if __name__ == '__main__':
    import sympy

    hs = sympy.sympify("x^3+3*x**2+m*x+m")
    b = sympy.Symbol('x')
    ts = sympy.Symbol('m')
    tim_tham_so_de_ham_so_don_tren_1_khoang_co_do_dai_k(hs, b, ts, 1).xuat_html('loi_giai.html')
