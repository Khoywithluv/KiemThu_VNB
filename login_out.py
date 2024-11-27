import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()

class TestShopVN:

    def test_dang_ki(self, driver):
        driver, wait = driver

        # Mở trang chủ
        driver.get("https://shopvnb.com/")

        # Đợi và nhấn vào nút Đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-action-item:nth-child(2) > .a-hea svg"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập"))).click()

        # Chuyển sang trang đăng ký
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng ký tại đây"))).click()

        # Điền thông tin đăng ký
        driver.find_element(By.ID, "ten").send_keys("Nguyễn Ngọc")
        driver.find_element(By.ID, "email").send_keys("ngockhoi1@gmail.com")
        driver.find_element(By.NAME, "so_dt").send_keys("0908624901")
        driver.find_element(By.ID, "password").send_keys("12345678")
        driver.find_element(By.ID, "re_password").send_keys("12345678")

        # Nhấn vào nút Đăng ký
        driver.find_element(By.CSS_SELECTOR, ".btn-style").click()

        # Kiểm tra URL sau khi đăng ký
        assert driver.current_url == "https://shopvnb.com/thanh-vien", "Không chuyển đến trang thành viên sau khi đăng ký"

        # Kiểm tra tiêu đề h1 với class "title-head widget-title" chứa văn bản "Thông tin tài khoản"
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.title-head.widget-title")))
        assert "thông tin tài khoản" in header.text.lower(), "Không tìm thấy tiêu đề 'Thông tin tài khoản'"

    def test_dang_nhap(self, driver, email="ngockhoi10112002@gmail.com", password="12345678"):
        driver, wait = driver

        # Mở trang chủ
        driver.get("https://shopvnb.com/")

        # Nhấn vào nút Đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-action-item:nth-child(2) > .a-hea svg"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập"))).click()

        # Nhập email và mật khẩu
        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.ID, "customer_password"))).send_keys(password)

        # Nhấp vào nút đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-style"))).click()

        # Kiểm tra tiêu đề hoặc nội dung cụ thể trên trang thành viên
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.title-head.widget-title")))
        assert "thông tin tài khoản" in header.text.lower(), "Không tìm thấy tiêu đề 'Thông tin tài khoản'"

        print("Đăng nhập thành công!")

        # Thêm thời gian chờ 5 giây trước khi kết thúc
        time.sleep(5)

    def test_dang_nhap_sai_mat_khau(self, driver, email="ngockhoi10112002@gmail.com", wrong_password="sai_mk"):
        driver, wait = driver

        # Mở trang chủ
        driver.get("https://shopvnb.com/")

        # Nhấn vào nút Đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-action-item:nth-child(2) > .a-hea svg"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập"))).click()

        # Nhập email và mật khẩu sai
        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.ID, "customer_password"))).send_keys(wrong_password)

        # Nhấp vào nút đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-style"))).click()

        # Kiểm tra thông báo lỗi
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.container p")))  # Kiểm tra thẻ div với class container bên trong thẻ p
        assert "mật khẩu không đúng" in error_message.text.lower(), " 'Mật khẩu không đúng'"

        print("Đăng nhập với mật khẩu sai")

    def test_dang_nhap_mat_khau_thieu(self, driver, email="ngockhoi10112002@gmail.com", wrong_password="12345"):
        driver, wait = driver

        # Mở trang chủ
        driver.get("https://shopvnb.com/")

        # Nhấn vào nút Đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-action-item:nth-child(2) > .a-hea svg"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập"))).click()

        # Nhập email và mật khẩu sai
        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.ID, "customer_password"))).send_keys(wrong_password)

        # Nhấp vào nút đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-style"))).click()

        # Kiểm tra thông báo lỗi
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.container p")))  # Kiểm tra thẻ div với class container bên trong thẻ p
        assert "mật khẩu phải tối thiểu 6 ký tự" in error_message.text.lower(), " 'mật khẩu phải tối thiểu 6 ký tự'"

        print("Đăng nhập với mật khẩu < 6")

    def test_dang_xuat(self, driver, email="ngockhoi10112002@gmail.com", password="12345678"):
        driver, wait = driver

        # Mở trang chủ
        driver.get("https://shopvnb.com/")

        # Nhấn vào nút Đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-action-item:nth-child(2) > .a-hea svg"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập"))).click()

        # Nhập email và mật khẩu
        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.ID, "customer_password"))).send_keys(password)

        # Nhấp vào nút đăng nhập
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-style"))).click()

        # Nhấp vào nút đăng xuất
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-action-item:nth-child(2) > .a-hea svg"))).click()
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-action-item:nth-child(2) > .a-hea svg"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Thoát"))).click()

        # Kiểm tra tiêu đề hoặc nội dung cụ thể trên trang chủ
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-action-item:nth-child(2) > .a-hea svg"))).click()
        assert wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập")))

        print("Đăng xuất thành công!")

        # Thêm thời gian chờ 5 giây trước khi kết thúc
        time.sleep(5)

class TestSubmitForm:

    def test_submit_form_success(self, driver):
        driver, wait = driver

        # Truy cập trang web có form
        driver.get("https://shopvnb.com/lien-he")

        # Điền thông tin vào form
        wait.until(EC.presence_of_element_located((By.NAME, "ten"))).send_keys("Nguyen Ngoc")
        driver.find_element(By.NAME, "email").send_keys("ngockhoi1@gmail.com")
        driver.find_element(By.NAME, "so_dt").send_keys("0908624901")
        driver.find_element(By.NAME, "noi_dung").send_keys("Đây là một thông điệp kiểm thử.")

        # Gửi form
        driver.find_element(By.CLASS_NAME, "btn-lienhe").click()

        # Kiểm tra thông báo sau khi gửi thành công
        time.sleep(5)
        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Thông tin liên hệ đã được gửi đi thành công')]")))
        assert "Thông tin liên hệ đã được gửi đi thành công" in success_message.text, "Thông báo gửi thành công không xuất hiện"

    def test_submit_form_missing_fields(self, driver):
        driver, wait = driver

        # Truy cập trang web có form
        driver.get("https://shopvnb.com/lien-he")

        # Chỉ điền vào một số trường, để trống trường email
        wait.until(EC.presence_of_element_located((By.NAME, "ten"))).send_keys("Nguyen Ngoc")
        driver.find_element(By.NAME, "so_dt").send_keys("0908624901")
        driver.find_element(By.NAME, "noi_dung").send_keys("Đây là một thông điệp kiểm thử.")

        # Gửi form
        driver.find_element(By.CLASS_NAME, "btn-lienhe").click()

        # Kiểm tra thông báo lỗi yêu cầu điền email
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
        assert "Vui lòng điền email" in error_message.text, "Thông báo lỗi về trường email không xuất hiện"

    def test_submit_form_invalid_email(self, driver):
        driver, wait = driver

        # Truy cập trang web có form
        driver.get("https://shopvnb.com/lien-he")

        # Điền thông tin vào form với email không hợp lệ
        wait.until(EC.presence_of_element_located((By.NAME, "ten"))).send_keys("Nguyen Ngoc")
        driver.find_element(By.NAME, "email").send_keys("email_khong_hop_le")
        driver.find_element(By.NAME, "so_dt").send_keys("0908624901")
        driver.find_element(By.NAME, "noi_dung").send_keys("Đây là một thông điệp kiểm thử.")

        # Gửi form
        driver.find_element(By.CSS_SELECTOR, ".submit-button").click()

        # Kiểm tra thông báo lỗi yêu cầu email hợp lệ
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
        assert "Vui lòng nhập email hợp lệ" in error_message.text, "Thông báo lỗi về email không hợp lệ không xuất hiện"

    def test_submit_form_empty_form(self, driver):
        driver, wait = driver

        # Truy cập trang web có form
        driver.get("https://shopvnb.com/lien-he")

        # Gửi form mà không điền bất kỳ trường nào
        driver.find_element(By.CSS_SELECTOR, ".submit-button").click()

        # Kiểm tra thông báo lỗi khi form trống
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
        assert "Vui lòng điền tất cả các trường" in error_message.text, "Thông báo lỗi khi form trống không xuất hiện"

    def test_submit_form_wrong_phone(self, driver):
        driver, wait = driver

        # Truy cập trang web có form
        driver.get("https://shopvnb.com/lien-he")

        wait.until(EC.presence_of_element_located((By.NAME, "ten"))).send_keys("Nguyen Ngoc")
        driver.find_element(By.NAME, "email").send_keys("ngockhoi1@gmail.com")
        driver.find_element(By.NAME, "so_dt").send_keys("090862490")
        driver.find_element(By.NAME, "noi_dung").send_keys("Đây là một thông điệp kiểm thử.")

        # Gửi form mà không điền bất kỳ trường nào
        driver.find_element(By.CSS_SELECTOR, ".submit-button").click()

        time.sleep(5)
        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Số điện thoại không đúng')]")))
        assert "Số điện thoại không đúng" in success_message.text, "Thông báo gửi thành công không xuất hiện"

class NavigationTest(unittest.TestCase):
    def test_navigation_to_contact_page(self):
        # Khởi tạo trình duyệt
        driver = webdriver.Chrome()
        driver.get("https://shopvnb.com")

        try:
            # Chờ cho liên kết "Liên hệ" có sẵn trước khi nhấp
            contact_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li.nav-item a.nav-link[title='Liên hệ']"))
            )
            contact_link.click()

            # Chờ URL của trang "Liên hệ" tải xong
            WebDriverWait(driver, 10).until(EC.url_contains("/lien-he"))

            # Kiểm tra URL hiện tại
            current_url = driver.current_url
            self.assertIn("/lien-he", current_url)
            print("Điều hướng thành công đến trang Liên hệ.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
        finally:
            # Đóng trình duyệt
            driver.quit()

    def test_scroll_to_bottom(self):
        # Khởi tạo trình duyệt
        driver = webdriver.Chrome()
        driver.get("https://shopvnb.com")  # Thay bằng URL của trang chính mà bạn muốn kiểm thử

        # Cuộn xuống cuối trang
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Nhấp vào liên kết "Chính sách đổi trả hoàn tiền"
        return_policy_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Chính sách đổi trả,hoàn tiền"))
        )
        return_policy_link.click()

        # Kiểm tra xem trang đã điều hướng đúng
        self.assertEqual(driver.current_url, "https://shopvnb.com/chinh-sach-doi-tra-hoan-tien.html")
        print("Điều hướng thành công đến trang Chính sách đổi trả hoàn tiền.")

        # Đóng trình duyệt
        driver.quit()

    def test_click_cart_link(self):
        # Khởi tạo trình duyệt
        driver = webdriver.Chrome()
        driver.get("https://shopvnb.com")  # Thay bằng URL của trang chính mà bạn muốn kiểm thử

        try:
            # Chờ cho liên kết "Giỏ hàng" có sẵn trước khi nhấp
            cart_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.a-hea[title='Giỏ hàng']"))
            )
            cart_link.click()

            # Chờ cho tiêu đề trang "Giỏ hàng" được tải xong
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title_cart span"))
            )

            # Kiểm tra tiêu đề của trang
            cart_title = driver.find_element(By.CSS_SELECTOR, "h1.title_cart span")
            self.assertEqual(cart_title.text.lower(), "giỏ hàng của bạn", "Tiêu đề không đúng.")
            print("Điều hướng thành công đến trang Giỏ hàng và tiêu đề đúng.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
        finally:
            # Đóng trình duyệt
            driver.quit()

    def test_navigation_to_product_page(self):
        # Khởi tạo trình duyệt
        driver = webdriver.Chrome()
        driver.get("https://shopvnb.com")  # Thay bằng URL của trang chính mà bạn muốn kiểm thử

        try:
            # Nhấp vào liên kết "Sản Phẩm"
            products_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link[title='Sản Phẩm']"))
            )
            products_link.click()

            # Nhấp vào liên kết "Vợt cầu lông Yonex"
            yonex_racket_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Vợt cầu lông Yonex"))
            )
            yonex_racket_link.click()

            # Kiểm tra xem URL hiện tại có đúng không
            self.assertEqual(driver.current_url, "https://shopvnb.com/vot-cau-long-yonex.html",
                             "URL không đúng sau khi điều hướng.")
            print("Điều hướng thành công đến trang Vợt cầu lông Yonex.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
        finally:
            # Đóng trình duyệt
            driver.quit()

    def test_navigation_between_product_pages(self):
        # Khởi tạo trình duyệt
        driver = webdriver.Chrome()
        driver.get("https://shopvnb.com")  # Thay bằng URL của trang chính mà bạn muốn kiểm thử

        try:
            # Nhấp vào liên kết "Sản Phẩm"
            products_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav-link[title='Sản Phẩm']"))
            )
            products_link.click()

            # Nhấp vào liên kết "Vợt cầu lông Yonex"
            yonex_racket_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Vợt cầu lông Yonex"))
            )
            yonex_racket_link.click()

            # Kiểm tra xem URL hiện tại có đúng không cho Vợt cầu lông Yonex
            self.assertEqual(driver.current_url, "https://shopvnb.com/vot-cau-long-yonex.html", "URL không đúng sau khi điều hướng đến Vợt cầu lông Yonex.")
            print("Điều hướng thành công đến trang Vợt cầu lông Yonex.")

            # Nhấp vào liên kết "Vợt cầu lông Yonex Astrox 99 Play"
            product_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Vợt Cầu Lông Yonex Astrox 99 Play"))
            )
            product_link.click()  # Nhấp vào liên kết sản phẩm

            # Kiểm tra xem URL hiện tại có đúng không cho Vợt cầu lông Yonex Astrox 99 Play
            self.assertEqual(driver.current_url, "https://shopvnb.com/vot-cau-long-yonex-astrox-99-play.html", "URL không đúng sau khi điều hướng đến Vợt cầu lông Yonex Astrox 99 Play.")
            print("Điều hướng thành công đến trang Vợt cầu lông Yonex Astrox 99 Play.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
        finally:
            # Đảm bảo rằng trình duyệt chỉ đóng sau khi mọi thao tác đã hoàn thành
            if driver:
                driver.quit()

class PriceValidationTest(unittest.TestCase):

    def test_price_validation(self):
        # Khởi tạo trình duyệt
        driver = webdriver.Chrome()
        driver.get("https://shopvnb.com/vot-cau-long-yonex.html")

        try:
            # Tìm giá tiền trên trang danh sách sản phẩm
            product_price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-info .price-box .price"))
            )
            product_price = product_price_element.text.strip()  # Lấy giá tiền

            # Nhấp vào sản phẩm để vào trang chi tiết
            product_link = driver.find_element(By.LINK_TEXT, "Vợt Cầu Lông Yonex Astrox 99 Game")
            product_link.click()

            # Chờ cho trang chi tiết tải và tìm giá tiền trên trang chi tiết
            detail_price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".price-box .price"))
            )
            detail_price = detail_price_element.text.strip()  # Lấy giá tiền từ trang chi tiết

            # So sánh giá tiền
            self.assertEqual(product_price, detail_price, "Giá tiền không khớp giữa danh sách và chi tiết sản phẩm.")
            time.sleep(5)
        finally:
            # Đóng trình duyệt
            driver.quit()

    def test_add_to_card(self):
        driver = webdriver.Chrome()
        driver.get("https://shopvnb.com/vot-cau-long-yonex.html")

        try:
            # Tìm giá tiền trên trang danh sách sản phẩm
            product_price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-info .price-box .price"))
            )
            product_price = product_price_element.text.strip()  # Lấy giá tiền

            # Nhấp vào sản phẩm để vào trang chi tiết
            product_link = driver.find_element(By.LINK_TEXT, "Vợt Cầu Lông Yonex Astrox 99 Game")
            product_link.click()


            size_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swatch-element.size-4U5"))
            )
            size_option.check()

            driver.execute_script("window.scrollTo(0, 1000)")
            num = 3
            for i in range (1,num):
                i += 1
                increase_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Tăng"]'))
                )
                increase_button.click()  # Nhấn nút để tăng số lượng sản phẩm

                time.sleep(2)  # Đợi một chút để xem sự thay đổi

                # Kiểm tra số lượng sản phẩm hiện tại (nếu cần)
                quantity_field = driver.find_element(By.ID, 'qtym')
                current_quantity = quantity_field.get_attribute('value')
                print(f"Số lượng sản phẩm hiện tại: {current_quantity}")

            # Nhấn "Thêm vào giỏ hàng" trên trang chi tiết
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn_add_cart.add_to_cart"))
            )

            # Nhấn vào nút "Thêm vào giỏ hàng"
            add_to_cart_button.click()

            #Tính tổng tiền
            ExpectedCost = product_price*3

            # Nhấp vào liên kết "Xem giỏ hàng" để mở giỏ hàng
            view_cart_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.checkout[title='Xem giỏ hàng']"))
            )
            view_cart_link.click()

            cart_total_price_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.total-price"))
            )
            cart_total_price = cart_total_price_element.text.strip()
            cart_total_price_value = float(cart_total_price.replace(".", "").replace(",", "").replace("₫", "").strip())

            # So sánh tổng giá tiền
            self.assertEqual(ExpectedCost, cart_total_price_value, "Tổng giá tiền trong giỏ không khớp.")
        finally:
            # Đóng trình duyệt
            driver.quit()

class DatHangTester:
    def test_dat_hang(self, driver):
        driver, wait = driver

        # Mở trang thanh toán
        driver.get("https://shopvnb.com/gio-hang/thanh-toan")

        # Điền thông tin người nhận hàng
        wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Nguyễn Ngọc Khôi")
        driver.find_element(By.NAME, "phone").send_keys("0925480768")
        driver.find_element(By.NAME, "address").send_keys("26/19/100 Lâm Hoành P. An Lạc Q. Bình Tân")
        driver.find_element(By.NAME, "email").send_keys("ngockhoi10112003@gmail.com")

        # Nhấn nút 'ĐẶT HÀNG'
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Kiểm tra thông báo xác nhận đặt hàng thành công
        confirmation_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-success-message")))
        assert "đặt hàng thành công" in confirmation_message.text.lower(), "Đặt hàng không thành công hoặc không có thông báo"

        print("Kiểm tra đặt hàng: Thành công")

        def test_sai(self, driver):
            driver, wait = driver

            # Mở trang thanh toán
            driver.get("https://shopvnb.com/gio-hang/thanh-toan")

            # Điền thông tin người nhận hàng
            wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Nguyễn Ngọc Khôi")
            driver.find_element(By.NAME, "phone").send_keys("09254807689")
            driver.find_element(By.NAME, "address").send_keys("26/19/100 Lâm Hoành P. An Lạc Q. Bình Tân")
            driver.find_element(By.NAME, "email").send_keys("ngockhoi10112003@gmail.com")

            # Nhấn nút 'ĐẶT HÀNG'
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            # Kiểm tra thông báo xác nhận đặt hàng thành công
            confirmation_message = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-success-message")))
            assert "đặt hàng thành công" in confirmation_message.text.lower(), "Đặt hàng không thành công hoặc không có thông báo"

            print("Kiểm tra đặt hàng: Thành công")

class TestShopVNSearch:

    def test_tim_kiem_khong_hop_le(self, driver):
        driver, wait = driver

        # Mở trang chủ
        driver.get("https://shopvnb.com/")

        # Nhập từ khóa tìm kiếm với 0 ký tự
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "tu_khoa")))
        search_box.clear()
        search_box.send_keys("")  # Nhập từ khóa rỗng

        # Nhấn nút "Tìm kiếm"
        search_button = driver.find_element(By.CLASS_NAME, "btn.icon-fallback-text")
        search_button.click()

        # Kiểm tra hiển thị thông báo lỗi hoặc trạng thái không tìm thấy
        try:
            error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
            assert "nhập từ khóa tìm kiếm" in error_message.text.lower(), "Không tìm thấy thông báo lỗi phù hợp"
            print("Kiểm tra tìm kiếm với từ khóa không hợp lệ: Thành công")
        except Exception as e:
            print(f"Kiểm tra tìm kiếm thất bại: {e}")

    def test_tim_kiem_ky_tu_dac_biet(self, driver):
        driver, wait = driver

        # Mở trang chủ
        driver.get("https://shopvnb.com/")

        # Nhập từ khóa tìm kiếm với ký tự đặc biệt "%%%%"
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "tu_khoa")))
        search_box.clear()
        search_box.send_keys("%%%%")  # Nhập từ khóa không hợp lệ

        # Nhấn nút "Tìm kiếm"
        search_button = driver.find_element(By.CLASS_NAME, "btn.icon-fallback-text")
        search_button.click()

        # Kiểm tra kết quả trả về khi tìm kiếm không hợp lệ
        try:
            no_result_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".no-results-message")))
            assert "không tìm thấy sản phẩm" in no_result_message.text.lower(), "Không tìm thấy thông báo kết quả phù hợp"
            print("Kiểm tra tìm kiếm với ký tự đặc biệt: Thành công")
        except Exception as e:
            print(f"Kiểm tra tìm kiếm thất bại: {e}")


