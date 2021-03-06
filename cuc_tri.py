import bat_dang_thuc
import dao_ham
import dinh_nghia
import hang_so
import huong_dan_giai
import ky_hieu_latex
import phuong_trinh
import phuong_trinh_bac_2
import tap_hop
import tinh_xac_dinh
import xu_ly_chuoi
import sympy

def tim_diem_cuc_tieu(ham_so, bien):
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien).dap_an
    dao_ham_cap_2 = dao_ham.tinh_dao_ham_cap_1(dao_ham_cap_1, bien).dap_an
    nghiem_dao_ham_cap_1 = phuong_trinh.tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien).dap_an
    nghiem_cuc_tieu = []
    for nghiem in nghiem_dao_ham_cap_1:
        if txd.contains(nghiem) is False:
            continue
        else:
            if dao_ham_cap_2.subs(bien, nghiem) > 0:
                nghiem_cuc_tieu.append(nghiem)
    dct = []
    for nghiem in nghiem_cuc_tieu:
        dct.append((nghiem, ham_so.subs(bien, nghiem)))
    return dct


def tim_diem_cuc_dai(ham_so, bien):
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien).dap_an
    dao_ham_cap_2 = dao_ham.tinh_dao_ham_cap_1(dao_ham_cap_1, bien).dap_an
    nghiem_dao_ham_cap_1 = phuong_trinh.tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien).dap_an
    nghiem_cuc_dai = []
    for nghiem in nghiem_dao_ham_cap_1:
        if txd.contains(nghiem) is False:
            continue
        else:
            if dao_ham_cap_2.subs(bien, nghiem) < 0:
                nghiem_cuc_dai.append(nghiem)
    dcd = []
    for nghiem in nghiem_cuc_dai:
        dcd.append((nghiem, ham_so.subs(bien, nghiem)))
    return dcd


def tim_tham_so_de_ham_so_khong_co_cuc_tri(ham_so, bien, tham_so):
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai("Tìm {0} để {1} không có cực trị".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))

    # ---------------------------Cau hoi----------
    cau_hoi_1 = huong_dan_giai.HoiDap("Khi nào thì hàm số không có cực trị ?")
    da_1 = huong_dan_giai.DapAnCauHoi(
        "Khi đạo hàm của hàm số có nghiệm kép hoặc vô nghiệm",
        [("f' = 0", "dao ham", "y' = 0"), "co", "nghiem kep", "vo nghiem"])
    da_2 = huong_dan_giai.DapAnCauHoi(
        "Khi đạo hàm của hàm số không có hai nghiệm phân biệt",
        [("f' = 0", "dao ham", "y' = 0"), " khong co", "nghiem phan biet"])
    gy_1 = "Có liên quan đến đạo hàm"
    gy_2 = "Nghiệm của đạo hàm như thế nào ?"
    cau_hoi_1.dap_an.append(da_1)
    cau_hoi_1.dap_an.append(da_2)
    cau_hoi_1.cac_goi_y.append(gy_1)
    cau_hoi_1.cac_goi_y.append(gy_2)

    loi_giai.cac_cau_hoi.append(cau_hoi_1)

    # ---------------Bai giai------------------------------
    # Buoc 1 tim tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = "Tìm tập xác định của hàm số"
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 Tinh dao ham cua ham so
    buoc_2 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.ten_loi_giai = "Tìm đạo hàm của hàm số"

    loi_giai.them_thao_tac(buoc_2)

    if phuong_trinh.loai_ham_so(ham_so,
                                bien) in hang_so.LoaiHamSo.CAC_HAM_PHAN_THUC:
        can_xet = phuong_trinh.lay_tu_so(ham_so)
    else:
        can_xet = buoc_2.dap_an

    # Buoc 3 Tim tham so de f' co 2 nghiem phan biet
    buoc_3 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_co_nghiem_kep_hoac_vo_nghiem(
        can_xet, bien, tham_so)
    buoc_3.ten_loi_giai = "Tìm {0} để đạo hàm có nghiệm kép hoặc vô nghiệm".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)))
    buoc_3.cac_buoc_giai = buoc_3.cac_buoc_giai
    loi_giai.them_thao_tac(buoc_3)

    # Buoc 4 tong hop
    buoc_4 = huong_dan_giai.LoiGiai("Tổng hợp kết quả và kết luận")
    buoc_4.them_thao_tac("Tổng hợp kết quả với tập xác định ta được:")
    tong_ket = tap_hop.tim_giao(buoc_1.dap_an, buoc_3.dap_an)
    buoc_4.them_thao_tac("Với {t} thì hàm số không có cực trị".format(
        t=xu_ly_chuoi.boc_mathjax("{ts} \in {tk}".format(
            ts=xu_ly_chuoi.tao_latex(tham_so),
            tk=xu_ly_chuoi.tao_latex(tong_ket)))))

    buoc_4.dap_an = tong_ket
    loi_giai.them_thao_tac(buoc_4)
    loi_giai.dap_an = tong_ket
    return loi_giai


def tim_phuong_trinh_duong_thang_di_qua_hai_diem_cuc_tri(ham_so, bien):
    """
    Can chia da thuc, thu vien chua ho tro
    :param ham_so: 
    :param bien: 
    :return: 
    """
    raise NotImplementedError


def tim_tham_so_de_ham_so_co_cuc_tri(ham_so, bien, tham_so):
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai("Tìm {0} để {1} có cực trị".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))

    # --------------Cac cau hoi -------------------------
    cau_hoi_1 = huong_dan_giai.HoiDap('Hàm số có cực trị khi nào ?')
    dap_an_cau_1 = huong_dan_giai.DapAnCauHoi(
        'Đạo hàm của hàm số có hai nghiệm phân biệt',
        [('dao ham', "f' = 0", "y' = 0"), 'co', 'nghiem phan biet'])
    cau_hoi_1.cac_goi_y.append('Có liên quan đến đạo hàm.')
    cau_hoi_1.cac_goi_y.append('Nghiệm của đạo hàm như thế nào ?')
    cau_hoi_1.dap_an.append(dap_an_cau_1)
    loi_giai.cac_cau_hoi.append(cau_hoi_1)

    # --------------------Dinh nghia su dung---------------------
    loi_giai.cac_dinh_nghia.append(dinh_nghia.DE_HAM_SO_CO_CUC_TRI)

    # ---------------------Bai toan mau---------------------
    hs_mau = sympy.sympify("x^3 - 3*m**2*x-2*m")
    bien_mau = sympy.Symbol('x')
    ts_mau = sympy.Symbol('m')

    # Neu bai mau khong trung voi bai hien tai
    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_ham_so_co_cuc_tri(
            hs_mau, bien_mau, ts_mau).xuat_html()

    # --------------------------Bai giai---------------------
    # Buoc 1 tim tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = "Tìm tập xác định của hàm số"
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 Tinh dao ham cua ham so
    buoc_2 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.ten_loi_giai = "Tìm đạo hàm của hàm số"

    loi_giai.them_thao_tac(buoc_2)

    if phuong_trinh.loai_ham_so(ham_so, bien) in hang_so.LoaiHamSo.HAM_DA_THUC:
        can_xet = phuong_trinh.lay_tu_so(ham_so)
    else:
        can_xet = buoc_2.dap_an

    # Buoc 3 Tim tham so de f' co 2 nghiem phan biet
    buoc_3 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(
        can_xet, bien, tham_so)
    buoc_3.ten_loi_giai = "Tìm {0} để đạo hàm có hai nghiệm phân biệt".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)))
    buoc_3.cac_buoc_giai = buoc_3.cac_buoc_giai
    loi_giai.them_thao_tac(buoc_3)

    # Buoc 4 tong hop
    buoc_4 = huong_dan_giai.LoiGiai("Tổng hợp kết quả và kết luận")
    buoc_4.them_thao_tac("Tổng hợp kết quả với tập xác định ta được:")
    tong_ket = tap_hop.tim_giao(buoc_1.dap_an, buoc_3.dap_an)
    buoc_4.them_thao_tac("Với {t} thì hàm số có cực trị".format(
        t=xu_ly_chuoi.boc_mathjax("{ts} \in {tk}".format(
            ts=xu_ly_chuoi.tao_latex(tham_so),
            tk=xu_ly_chuoi.tao_latex(tong_ket)))))

    buoc_4.dap_an = tong_ket
    loi_giai.them_thao_tac(buoc_4)
    loi_giai.dap_an = tong_ket
    return loi_giai


def tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung(ham_so, bien, tham_so):
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm {0} để {1} có cực trị nằm ở hai phía của trục tung".format(
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))

    # todo: Chua test
    # ---------------------Cau hoi -----------------------
    # todo: Can bo sung them cau hoi (neu co)
    ch_1 = huong_dan_giai.HoiDap("Đầu tiên ta phải làm gì ?")
    da_1 = huong_dan_giai.DapAnCauHoi("Tìm tham số để hàm số có cực trị",
                                      ["tim", "co cuc tri"])
    ch_1.cac_goi_y.append("Để có cực trị năm ở hai phía trục hoành , thì ta phải có gì trước?")
    ch_1.dap_an.append(da_1)
    loi_giai.cac_cau_hoi.append(ch_1)
    loi_giai.cac_cau_hoi.append(ch_1)

    # --------------------Dinh ly-----------------------
    loi_giai.cac_dinh_nghia.append(
        dinh_nghia.DE_HAM_SO_CO_CUC_TRI_NAM_O_HAI_PHIA_TRUC_TUNG)

    # --------------------------Bai toan mau----------------------
    # todo: Can kiem tra lai xem mau nay duoc khong
    hs_mau = sympy.sympify("x^3 - 3*m**2*x-2*m")
    bien_mau = sympy.Symbol('x')
    ts_mau = sympy.Symbol('m')

    # Neu bai mau khong trung voi bai hien tai
    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung(
            hs_mau, bien_mau, ts_mau).xuat_html()

    # -------------------Bai giai ----------------------------
    # Buoc 1 tim tham so de ham so co cuc tri
    buoc_1 = tim_tham_so_de_ham_so_co_cuc_tri(ham_so, bien, tham_so)
    buoc_1.ten_loi_giai = 'Tìm {ts} để hàm số có cực trị'.format(
        ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)))
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 tim tham so de tich 2 nghiem am
    nghiem = buoc_1.cac_buoc_giai[2].cac_buoc_giai[2].dap_an
    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')
    dieu_kien = bat_dang_thuc.nho_hon(nghiem_1 * nghiem_2, 0)
    buoc_2 = huong_dan_giai.LoiGiai('Giải bất đẳng thức {bdt} tìm {ts}'.format(
        bdt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)),
        ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    # The bien
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_1, nghiem[0])
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_2, nghiem[1])

    # Giai bat dang thuc
    giai_bat_dang_thuc = bat_dang_thuc.giai_bat_dang_thuc_lg(dieu_kien,
                                                             tham_so)
    buoc_2.cac_buoc_giai += giai_bat_dang_thuc.cac_buoc_giai
    buoc_2.dap_an = giai_bat_dang_thuc.dap_an

    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3 tong hop
    buoc_3 = huong_dan_giai.LoiGiai("Tổng hợp kết quả và kết luận")
    buoc_3.them_thao_tac("Tổng hợp 2 bước trên ta được:")
    tong_ket = tap_hop.tim_giao(buoc_1.dap_an, buoc_2.dap_an)
    buoc_3.them_thao_tac(
        "Với {ts} thì hàm số có cực trị nằm ở hai phía trục tung ".format(
            ts=xu_ly_chuoi.boc_mathjax("{ts} \in {tk}".format(
                ts=xu_ly_chuoi.tao_latex(tham_so),
                tk=xu_ly_chuoi.tao_latex(tong_ket)))))

    buoc_3.dap_an = tong_ket
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.dap_an = tong_ket
    return loi_giai


def tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_hoanh(ham_so, bien, tham_so):
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm {0} để {1} có cực trị nằm ở hai phía của trục hoành".format(
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))

    # todo: Test
    # ---------------------------CAU HOI------------------------------
    # todo: them cau hoi
    ch_1 = huong_dan_giai.HoiDap("Đầu tiên ta phải làm gì ?")
    da_1 = huong_dan_giai.DapAn("Tìm tham số để hàm số có cực trị",
                                ["tim", "co cuc tri"])
    gy_1 = "Để có cực trị năm ở hai phía trục hoành , thì ta phải có gì trước?"
    ch_1.dap_an.append(da_1)
    ch_1.cac_goi_y.append(gy_1)
    loi_giai.cac_cau_hoi.append(ch_1)

    # ----------------------------DINH NGHIA-----------------------
    loi_giai.cac_dinh_nghia.append(
        dinh_nghia.DE_HAM_SO_CO_CUC_TRI_NAM_O_HAI_PHIA_TRUC_HOANH)

    # -----------------------------BAI TOAN MAU---------------------
    hs_mau = sympy.sympify("x^3 - 3*m**2*x-2*m")
    bien_mau = sympy.Symbol('x')
    ts_mau = sympy.Symbol('m')

    # Neu bai mau khong trung voi bai hien tai
    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung(
            hs_mau, bien_mau, ts_mau).xuat_html()

    # -------------------------------LOI GIAI--------------------------------
    # Buoc 1 tim tham so de ham so co cuc tri
    buoc_1 = tim_tham_so_de_ham_so_co_cuc_tri(ham_so, bien, tham_so)
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 tim tham so de tich 2 nghiem am
    nghiem = buoc_1.cac_buoc_giai[2].cac_buoc_giai[2].dap_an
    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')
    dieu_kien = bat_dang_thuc.nho_hon(nghiem_1 * nghiem_2, 0)
    buoc_2 = huong_dan_giai.LoiGiai("Tìm nghiệm của bất đẳng thức {0}".format(
        xu_ly_chuoi.boc_mathjax("f({0})f({1})<0".format(
            xu_ly_chuoi.tao_latex(nghiem_1), xu_ly_chuoi.tao_latex(
                nghiem_2)))))

    # In ra dieu kien
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax("f({0})f({1})<0".format(
            xu_ly_chuoi.tao_latex(nghiem_1), xu_ly_chuoi.tao_latex(nghiem_2))))

    # Thay cac nghiem vao
    f_nghiem_1 = phuong_trinh.the_bien(ham_so, bien, nghiem_1)
    f_nghiem_2 = phuong_trinh.the_bien(ham_so, bien, nghiem_2)

    dieu_kien = bat_dang_thuc.nho_hon(f_nghiem_1 * f_nghiem_2, 0)

    # In ra dieu kien sau khi thay nghiem
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(dieu_kien)))

    # Thay bien vao
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_1, nghiem[0])
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_2, nghiem[1])

    # In ra dieu kien sau khi thay bien
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giai bat dang thuc
    giai_dieu_kien = bat_dang_thuc.giai_bat_dang_thuc_lg(dieu_kien, tham_so)
    buoc_2.cac_buoc_giai += giai_dieu_kien.cac_buoc_giai
    buoc_2.dap_an = giai_dieu_kien.dap_an

    loi_giai.them_thao_tac(buoc_2)

    # buoc 3 tong hop ket qua
    buoc_3 = huong_dan_giai.LoiGiai("Tổng hợp kết quả và kết luận")
    buoc_3.them_thao_tac("Tổng hợp kết quả của hai bước trước ta được:")
    tong_hop = tap_hop.tim_giao(buoc_1.dap_an, buoc_2.dap_an)
    buoc_3.them_thao_tac(
        "Với {ts} thì hàm số có cực trị nằm ở hai phía trục hoành".format(
            ts=xu_ly_chuoi.boc_mathjax("{ts} \in {th}".format(
                ts=xu_ly_chuoi.tao_latex(tham_so),
                th=xu_ly_chuoi.tao_latex(tong_hop)))))

    buoc_3.dap_an = tong_hop

    loi_giai.them_thao_tac(buoc_3)
    loi_giai.dap_an = tong_hop
    return loi_giai


def tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem(ham_so, bien, tham_so,
                                                   diem):
    """
    Tim ham so de ham so dat cuc tri tai mot diem
    :param ham_so: Ham bac ba, bac 4, nhat bien,huu ty
    :param bien: 
    :param tham_so: 
    :param diem: Diem dat cuc tri
    :return: 
    """
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        'Tìm {ts} để hàm số {hs} có cực trị tại điểm {d}'.format(
            ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f)),
            d=xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem)))))
    # ---------------------CAU HOI-----------------------------
    ch1 = huong_dan_giai.HoiDap(
        "Để hàm số đạt cực trị tại một điểm thì đạo hàm tại điểm đó thế nào ?")
    da1 = huong_dan_giai.DapAnCauHoi("Có nghiệm", ['co nghiem'])
    da11 = huong_dan_giai.DapAnCauHoi("Bằng 0", [('bang 0', '=0', '= 0')])
    ch1.dap_an.append(da1)
    ch1.dap_an.append(da11)
    loi_giai.cac_cau_hoi.append(ch1)

    # ----------------------------DINH NGHIA----------------------------
    loi_giai.cac_dinh_nghia.append(
        dinh_nghia.DE_HAM_SO_DAT_CUC_TRI_TAI_MOT_DIEM)

    # ----------------------------BAI TOAN MAU-----------------
    hs_mau = sympy.sympify("x^3 + m*x + 2")
    bien_mau = sympy.Symbol('x')
    ts_mau = sympy.Symbol('m')
    diem_mau = 1

    # Neu bai mau khong trung voi bai hien tai
    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem(
            hs_mau, bien_mau, ts_mau, diem_mau).xuat_html()

    # ----------------LOI GIAI------------------------------
    # buoc 1 : Tinh dao ham
    buoc_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm đạo hàm của hàm số'
    loi_giai.them_thao_tac(buoc_1)

    # buoc 2 : de ham so dat cuc tri tai x0 , f'(x0) = 0
    pt = bat_dang_thuc.bang(phuong_trinh.tao_ten_ham('f', diem), 0)
    buoc_2 = huong_dan_giai.LoiGiai(
        'Tìm {ts} để {pt}'.format(
            ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            pt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))

    # buoc 2.1 thay x0 vao
    buoc_2_1 = phuong_trinh.thay_bien(buoc_1.dap_an, bien, diem)

    # Buoc 2.2  gia pt
    buoc_2_2 = phuong_trinh.giai_phuong_trinh(buoc_2_1.dap_an, tham_so)

    buoc_2.dap_an = buoc_2_2.dap_an
    buoc_2.them_thao_tac(buoc_2_1)
    buoc_2.them_thao_tac(buoc_2_2)
    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3: Ket luan
    buoc_3 = huong_dan_giai.LoiGiai('Kết luận')
    buoc_3.them_thao_tac(
        'Vậy với {ts} thì hàm số có cực trị tại điểm {d}'.format(
            ts=xu_ly_chuoi.boc_mathjax('{t}={n}'.format(
                t=xu_ly_chuoi.tao_latex(tham_so),
                n=xu_ly_chuoi.tao_ngoac_nhon(buoc_2.dap_an))),
            d=xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem)))))
    loi_giai.dap_an = buoc_2.dap_an
    loi_giai.them_thao_tac(buoc_3)
    return loi_giai


# todo: them cau hoi , dinh nghia ,bai toan mau
def tim_tham_so_de_ham_so_dat_cuc_dai_tai_mot_diem(ham_so, bien, tham_so,
                                                   diem):
    """
    Tim tham so de ham so dat cuc dai tai mot diem
    Dang ham so : Bac 3 , Bac 4 
    Co tham so
    :return: LoiGiai
    """
    # Loi giai
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        'Tìm {ts} để hàm số {hs} đạt cực đại tại điểm {d}'.format(
            ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f)),
            d=xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem)))))
    # ---------------------CAU HOI-----------------------------
    ch1 = huong_dan_giai.HoiDap(
        "Để biết cực trị là cực đại hay cực tiểu ta cần làm gì?")
    da1 = huong_dan_giai.DapAnCauHoi("Xét đạo hàm cấp 2",
                                     ['dao ham', ('hai', '2')])
    ch1.dap_an.append(da1)
    ch1.cac_goi_y.append('Xét đạo hàm ...')
    loi_giai.cac_cau_hoi.append(ch1)

    ch2 = huong_dan_giai.HoiDap(
        "Để cực trị là cực đại thì đạo hàm cấp 2 tại điểm đó …")
    da2 = huong_dan_giai.DapAnCauHoi("Nhỏ hơn 0", [('nho hon', '<'), ('khong', '0')])
    ch2.dap_an.append(da2)
    ch2.cac_goi_y.append('Quan hệ như thế nào với 0?')
    ch2.cac_goi_y.append('Nhỏ hơn 0 hay lớn hơn 0 ?')
    loi_giai.cac_cau_hoi.append(ch2)

    # ----------------------------DINH NGHIA----------------------------
    loi_giai.cac_dinh_nghia.append(
        dinh_nghia.DE_HAM_SO_CO_CUC_DAI_TAI_MOT_DIEM)

    # ----------------------------BAI TOAN MAU-----------------
    hs_mau = sympy.sympify("x**3 + m*x + 2")
    bien_mau = sympy.Symbol('x')
    ts_mau = sympy.Symbol('m')
    diem_mau = 1

    # Neu bai mau khong trung voi bai hien tai
    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_ham_so_dat_cuc_dai_tai_mot_diem(
            hs_mau, bien_mau, ts_mau, diem_mau).xuat_html()

    # -----------BAI GIAI--------
    buoc_1 = tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem(ham_so, bien,
                                                            tham_so, diem)
    buoc_1.ten_loi_giai = 'Tìm {ts} để hàm số có cực trị tại {d}'.format(
        ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        d=xu_ly_chuoi.boc_mathjax(
            xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem))))
    loi_giai.them_thao_tac(buoc_1)

    # Ham bac ba hoac bac bon
    if phuong_trinh.loai_ham_so(
            ham_so, bien
    ) in [hang_so.LoaiHamSo.HAM_BAC_BA, hang_so.LoaiHamSo.HAM_BAC_BON]:

        # Buoc 2 : Tinh dao ham cap hai
        buoc_2 = dao_ham.tinh_dao_ham_cap_2(buoc_1.cac_buoc_giai[0].dap_an,
                                            bien)
        buoc_2.ten_loi_giai = "Tính đạo hàm cấp hai của hàm số"
        loi_giai.them_thao_tac(buoc_2)

        # Buoc 3: Xet dau dao ham cap 2 tai diem
        buoc_3 = huong_dan_giai.LoiGiai(
            "Xét dấu đạo hàm cấp 2 của hàm số tại {d} và {ts}".format(
                d=xu_ly_chuoi.boc_mathjax(
                    xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem))),
                ts=xu_ly_chuoi.boc_mathjax("m={b1_da}".format(
                    b1_da=xu_ly_chuoi.tao_ngoac_nhon(buoc_1.dap_an)))))

        # Buoc 3_1 : Thay bien
        buoc_3_1 = phuong_trinh.thay_bien(buoc_2.dap_an, bien, diem)
        buoc_3_1.ten_loi_giai = "Thế {b} vào".format(b=xu_ly_chuoi.boc_mathjax(
            xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem))))
        buoc_3.them_thao_tac(buoc_3_1)

        # Buoc 3_2 : The tham so tim duoc
        buoc_3_2 = huong_dan_giai.LoiGiai("Thế {ts} vào".format(
            ts=xu_ly_chuoi.boc_mathjax("m={b1_da}".format(
                b1_da=xu_ly_chuoi.tao_ngoac_nhon(buoc_1.dap_an)))))
        ket_qua = list()
        for ts in buoc_1.dap_an:
            the_ts = phuong_trinh.thay_bien(buoc_3_1.dap_an, tham_so, ts)
            buoc_3.dap_an = the_ts
            buoc_3_2.cac_buoc_giai += the_ts.cac_buoc_giai
            if the_ts.dap_an < 0:
                buoc_3_2.cac_buoc_giai[-1] += xu_ly_chuoi.boc_mathjax('<0')
                buoc_3_2.them_thao_tac('Vậy hàm số đạt cực đại tại điểm này')
                ket_qua.append(ts)
            elif the_ts.dap_an > 0:
                buoc_3_2.cac_buoc_giai[-1] += xu_ly_chuoi.boc_mathjax('>0')
                buoc_3_2.them_thao_tac('Vậy hàm số đạt cực tiểu tại điểm này')
            else:
                buoc_3_2.them_thao_tac(
                    'Vậy hàm số đạt không có cực trị tại điểm này')
        buoc_3.them_thao_tac(buoc_3_2)
        buoc_3.dap_an = buoc_3_2.dap_an
        loi_giai.them_thao_tac(buoc_3)

        # Buoc 4: Ket luan
        buoc_4 = huong_dan_giai.LoiGiai('Kết luận')
        if ket_qua == []:
            buoc_4.them_thao_tac(
                'Vậy không có giá trị nào của {ts} làm hàm số đạt cực đại tại điểm {d}'.
                format(
                    ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
                    d=xu_ly_chuoi.boc_mathjax(
                        xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien,
                                                                 diem)))))
        else:
            buoc_4.them_thao_tac(
                'Vậy với {ts} thì hàm số đạt cực đại tại điểm {d}'.format(
                    ts=xu_ly_chuoi.boc_mathjax('{ts}={kq}'.format(
                        ts=xu_ly_chuoi.tao_latex(tham_so),
                        kq=xu_ly_chuoi.tao_ngoac_nhon(ket_qua))),
                    d=xu_ly_chuoi.boc_mathjax(
                        xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien,
                                                                 diem)))))
        loi_giai.them_thao_tac(buoc_4)
    else:
        raise ValueError
    return loi_giai


# todo: test
def tim_tham_so_de_ham_so_dat_cuc_tieu_tai_mot_diem(ham_so, bien, tham_so,
                                                    diem):
    """
    Tim tham so de ham so dat cuc tieu tai mot diem
    Dang ham so : Bac 3 , Bac 4 
    Co tham so
    :return: LoiGiai
    """
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        'Tìm {ts} để hàm số {hs} đạt cực đại tại điểm {d}'.format(
            ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f)),
            d=xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem)))))
    # ------------------------CAU HOI-----------------------------
    ch1 = huong_dan_giai.HoiDap(
        "Để biết cực trị là cực đại hay cực tiều ta cần làm gì?")
    da1 = huong_dan_giai.DapAnCauHoi("Xét đạo hàm cấp 2",
                                     ['dao ham', ('hai', '2')])
    ch1.dap_an.append(da1)
    ch1.cac_goi_y.append('Xét đạo hàm ...')
    loi_giai.cac_cau_hoi.append(ch1)

    ch2 = huong_dan_giai.HoiDap(
        "Để cực trị là cực tiểu thì đạo hàm cấp 2 tại điểm đó …")
    da2 = huong_dan_giai.DapAnCauHoi("Lớn hơn 0", [('lớn hon 0', '>0')])
    ch2.dap_an.append(da2)
    ch2.cac_goi_y.append('Đạo hàm có nghiệm tại đó')
    ch2.cac_goi_y.append('Quan hệ như thế nào với 0?')
    loi_giai.cac_cau_hoi.append(ch2)
    # ---------------------DINH NGHIA------------------------------
    loi_giai.cac_dinh_nghia.append(
        dinh_nghia.DE_HAM_SO_CO_CUC_TIEU_TAI_MOT_DIEM)

    # ------------------------BAI TOAN MAU------------------------------
    hs_mau = sympy.sympify("x^3 + m*x + 2")
    bien_mau = sympy.Symbol('x')
    ts_mau = sympy.Symbol('m')
    diem_mau = 1

    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_ham_so_dat_cuc_tieu_tai_mot_diem(
            hs_mau, bien_mau, ts_mau, diem_mau).xuat_html()

    # ----------------------LOI GIAI-------------------------
    buoc_1 = tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem(ham_so, bien,
                                                            tham_so, diem)
    buoc_1.ten_loi_giai = 'Tìm {ts} để hàm số có cực trị tại {d}'.format(
        ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        d=xu_ly_chuoi.boc_mathjax(
            xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem))))
    loi_giai.them_thao_tac(buoc_1)

    # Ham bac ba hoac bac bon
    if phuong_trinh.loai_ham_so(
            ham_so, bien
    ) in [hang_so.LoaiHamSo.HAM_BAC_BA, hang_so.LoaiHamSo.HAM_BAC_BON]:

        # Buoc 2 : Tinh dao ham cap hai
        buoc_2 = dao_ham.tinh_dao_ham_cap_2(buoc_1.cac_buoc_giai[0].dap_an,
                                            bien)
        buoc_2.ten_loi_giai = "Tính đạo hàm cấp hai của hàm số"
        loi_giai.them_thao_tac(buoc_2)

        # Buoc 3: Xet dau dao ham cap 2 tai diem
        buoc_3 = huong_dan_giai.LoiGiai(
            "Xét dấu đạo hàm cấp 2 của hàm số tại {d} và {ts}".format(
                d=xu_ly_chuoi.boc_mathjax(
                    xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem))),
                ts=xu_ly_chuoi.boc_mathjax("m={b1_da}".format(
                    b1_da=xu_ly_chuoi.tao_ngoac_nhon(buoc_1.dap_an)))))

        # Buoc 3_1 : Thay bien
        buoc_3_1 = phuong_trinh.thay_bien(buoc_2.dap_an, bien, diem)
        buoc_3_1.ten_loi_giai = "Thế {b} vào".format(b=xu_ly_chuoi.boc_mathjax(
            xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem))))
        buoc_3.them_thao_tac(buoc_3_1)

        # Buoc 3_2 : The tham so tim duoc
        buoc_3_2 = huong_dan_giai.LoiGiai("Thế {ts} vào".format(
            ts=xu_ly_chuoi.boc_mathjax("m={b1_da}".format(
                b1_da=xu_ly_chuoi.tao_ngoac_nhon(buoc_1.dap_an)))))
        ket_qua = list()
        for ts in buoc_1.dap_an:
            the_ts = phuong_trinh.thay_bien(buoc_3_1.dap_an, tham_so, ts)
            buoc_3_2.cac_buoc_giai += the_ts.cac_buoc_giai
            if the_ts.dap_an < 0:
                buoc_3_2.cac_buoc_giai[-1] += xu_ly_chuoi.boc_mathjax('<0')
                buoc_3_2.them_thao_tac('Vậy hàm số đạt cực đại tại điểm này')
            elif the_ts.dap_an > 0:
                buoc_3_2.cac_buoc_giai[-1] += xu_ly_chuoi.boc_mathjax('>0')
                buoc_3_2.them_thao_tac('Vậy hàm số đạt cực tiểu tại điểm này')
                ket_qua.append(ts)
            else:
                buoc_3_2.them_thao_tac(
                    'Vậy hàm số đạt không có cực trị tại điểm này')
        buoc_3.them_thao_tac(buoc_3_2)
        loi_giai.them_thao_tac(buoc_3)

        # Buoc 4: Ket luan
        buoc_4 = huong_dan_giai.LoiGiai('Kết luận')
        if ket_qua == []:
            buoc_4.them_thao_tac(
                'Vậy không có giá trị nào của {ts} làm hàm số đạt cực tiểu tại điểm {d}'.
                format(
                    ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
                    d=xu_ly_chuoi.boc_mathjax(
                        xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien,
                                                                 diem)))))
        else:
            buoc_4.them_thao_tac(
                'Vậy với {ts} thì hàm số đạt cực tiểu tại điểm {d}'.format(
                    ts=xu_ly_chuoi.boc_mathjax('{ts}={kq}'.format(
                        ts=xu_ly_chuoi.tao_latex(tham_so),
                        kq=xu_ly_chuoi.tao_ngoac_nhon(ket_qua))),
                    d=xu_ly_chuoi.boc_mathjax(
                        xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien,
                                                                 diem)))))
        loi_giai.them_thao_tac(buoc_4)
    else:
        raise ValueError
    return loi_giai


# todo: them dang toan
def tim_tham_so_de_ham_so_co_dung_mot_cuc_tri(ham_so, bien, tham_so):
    loi_giai = huong_dan_giai.LoiGiai('Tìm {ts} để {hs} có đúng một cực trị')
    raise NotImplementedError


# Thu nghiem
if __name__ == "__main__":
    import sympy

    x = sympy.Symbol('x')
    m = sympy.Symbol('m')

    def tim_tham_so_de_ham_so_co_cuc_tri_test():
        hs = sympy.sympify("x^3 - 3*m**2*x-2*m")
        tim_tham_so_de_ham_so_co_cuc_tri(hs, x, m).xuat_html("loi_giai.html")

    def tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung_test():
        hs = sympy.sympify("x^3 - 3*m**2*x-2*m")
        tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung(
            hs, x, m).xuat_html("loi_giai.html")

    def tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_hoanh_test():
        hs = sympy.sympify("x^3 - 3*m**2*x-2*m")
        tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_hoanh(
            hs, x, m).xuat_html("loi_giai.html")

    def tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem_test():
        hs = sympy.sympify("(x^3)/3 - x**2 +(2*m+1)*x-5")
        d = -1
        tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem(
            hs, x, m, d).xuat_html("loi_giai.html")

    def tim_tham_so_de_ham_so_dat_cuc_dai_tai_mot_diem_test():
        hs = sympy.sympify("(x^3)/3 - x**2 +(2*m+1)*x-5")
        d = -1
        # hs = sympy.sympify("x^3+m*x+2")
        # d = 1
        tim_tham_so_de_ham_so_dat_cuc_dai_tai_mot_diem(
            hs, x, m, d).xuat_html("loi_giai.html")

    def tim_tham_so_de_ham_so_dat_cuc_tieu_tai_mot_diem_test():
        # hs = sympy.sympify("(x^3)/3 - x**2 +(2*m+1)*x-5")
        # d = -1
        hs = sympy.sympify("x^3+m*x+2")
        d = 1
        tim_tham_so_de_ham_so_dat_cuc_tieu_tai_mot_diem(
            hs, x, m, d).xuat_html("loi_giai.html")

    def tim_tham_so_de_ham_so_khong_co_cuc_tri_test():
        # hs = sympy.sympify("x^3 - 3*m**2*x-2*m")
        hs = (x**2 + m * x + 1) / (x + m)
        tim_tham_so_de_ham_so_khong_co_cuc_tri(hs, x,
                                               m).xuat_html("loi_giai.html")

    # tim_tham_so_de_ham_so_co_cuc_tri_test()
    # tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem_test()
    tim_tham_so_de_ham_so_dat_cuc_dai_tai_mot_diem_test()
    # tim_tham_so_de_ham_so_dat_cuc_tieu_tai_mot_diem_test()
    # tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung_test()
    # tim_tham_so_de_ham_so_khong_co_cuc_tri_test()
