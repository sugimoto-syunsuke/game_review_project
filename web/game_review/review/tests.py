import socket
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .models import Game, ReviewPost
from accounts.models import CustomUser

@override_settings(ALLOWED_HOSTS=['*'])
class LoginTest(StaticLiveServerTestCase):
    host = '0.0.0.0' #外部アクセスを許可するために0.0.0.0をバインドする
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # ホストを外部からアクセス可能な Web サーバーのアドレスに設定する
        cls.host = socket.gethostbyname(socket.gethostname())
        cls.selenium = webdriver.Remote(
                        command_executor="http://selenium:4444/wd/hub",
                        options=webdriver.ChromeOptions()
                        )
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_signup_success(self):
        # TOPページを開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        # サインアップ画面へ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "今すぐサインアップ")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Sign up', self.selenium.title)
        # アカウント情報を入れ、サインアップ検証
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys('unittest')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys('unittest@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.send_keys('Selenium2023')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.send_keys('Selenium2023')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Registration Complete', self.selenium.title)
        print("正常テスト：サインアップ処理　完了")
        
    def test_signup_failure(self):
        # テスト用に必要なオブジェクトを追加する
        CustomUser.objects.create(username='nguser', email='unittest@test.com', password='Selenium2023')
        # TOPページを開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        # サインアップ画面へ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "今すぐサインアップ")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Sign up', self.selenium.title)
        # ユーザ名無入力のバリデーションチェック
        # username_input = self.selenium.find_element(By.NAME, "username")
        # username_input.send_keys('unittest')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys('unittest@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.send_keys('Selenium2023')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.send_keys('Selenium2023')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # メールアドレス無入力のバリデーションチェック
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('unittest')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.clear()
        password1_input.send_keys('Selenium2023')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.clear()
        password2_input.send_keys('Selenium2023')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # パスワード無入力のバリデーションチェック
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('unittest')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys('unittest@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.clear()
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.clear()
        password2_input.send_keys('Selenium2023')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # パスワード（確認用）無入力のバリデーションチェック
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('unittest')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys('unittest@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.clear()
        password1_input.send_keys('Selenium2023')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.clear()
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # ユーザ名重複のバリデーションチェック
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('nguser')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys('unittest@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.clear()
        password1_input.send_keys('Selenium2023')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.clear()
        password2_input.send_keys('Selenium2023')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("同じユーザー名が既に登録済みです。", self.selenium.find_element(By.TAG_NAME, "body").text)
        # メールアドレスに@を含まない場合のバリデーションチェック
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('unittest')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys('unittest')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.clear()
        password1_input.send_keys('Selenium2023')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.clear()
        password2_input.send_keys('Selenium2023')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # パスワードが短すぎる場合のバリデーション
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('unittest')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys('unittest@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.clear()
        password1_input.send_keys('aaaaaaa')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.clear()
        password2_input.send_keys('aaaaaaa')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("このパスワードは短すぎます。最低 8 文字以上必要です。", self.selenium.find_element(By.TAG_NAME, "body").text)
        # ユーザ名とパスワードが同じ場合のバリデーション
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('tanaka2023')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys('tanaka2023@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.clear()
        password1_input.send_keys('tanaka2023')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.clear()
        password2_input.send_keys('tanaka2023')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("このパスワードは ユーザー名 と似すぎています。", self.selenium.find_element(By.TAG_NAME, "body").text)
        # パスワードが一般的すぎる場合のバリデーションチェック
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('tanaka2023')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys('tanaka2023@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.clear()
        password1_input.send_keys('test1234')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.clear()
        password2_input.send_keys('test1234')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページ遷移していないか検証
        self.assertEquals('Sign up', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("このパスワードは一般的すぎます。", self.selenium.find_element(By.TAG_NAME, "body").text)
        print("バリデーションチェック：サインアップ処理　完了")
        
    def test_login_success(self):
        self.test_signup_success()
        # ログイン画面へ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "ログインはこちら")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Log in', self.selenium.title)
        # ログイン情報を入れ、ログイン検証
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys('unittest')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('Selenium2023')
        self.selenium.find_element(By.CLASS_NAME, "btn").click()
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        print("正常テスト：ログイン処理　完了")
    
    def test_login_failure(self):
        self.test_signup_success()
        # ログイン画面へ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "ログインはこちら")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Log in', self.selenium.title)
        # 存在しないIDでログインできないことを確認
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('Unittest')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('Selenium2023')
        self.selenium.find_element(By.CLASS_NAME, "btn").click()
        # ページタイトルの検証
        self.assertEquals('Log in', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("ユーザ名とパスワードが一致しません", self.selenium.find_element(By.TAG_NAME, "body").text)
        # パスワード不一致でログインできないことを確認
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('Unittest')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('selenium2023')
        self.selenium.find_element(By.CLASS_NAME, "btn").click()
        # ページタイトルの検証
        self.assertEquals('Log in', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("ユーザ名とパスワードが一致しません", self.selenium.find_element(By.TAG_NAME, "body").text)
        print("バリデーションチェック：ログイン処理　完了")
    
    def test_review_regist_success(self):
        # テスト用に必要なオブジェクトを追加する
        Game.objects.create(title='テスト用ゲーム', image1='../static/img/test.png')
        self.test_login_success()
        # レビュー投稿ページへ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "投稿する")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # 投稿するレビュー情報を入れ、投稿ボタンを押下する
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.send_keys('65')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post Success', self.selenium.title)
        print("正常テスト：レビュー登録処理　完了")
 
    def test_review_regist_failure(self):
        # テスト用に必要なオブジェクトを追加する
        Game.objects.create(title='テスト用ゲーム', image1='../static/img/test.png')
        self.test_login_success()
        # レビュー投稿ページへ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "投稿する")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # ゲーム未選択で投稿できないことを確認
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(0)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        score_input.send_keys('65')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # レビュータイトル未入力で投稿できないことを確認
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        score_input.send_keys('65')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # レビューコメント未入力で投稿できないことを確認
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        score_input.send_keys('65')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # レビュー点数未入力で投稿できないことを確認
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # レビュー点数がマイナスで投稿できないことを確認
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        score_input.send_keys('-1')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("この値は 0 以上でなければなりません。", self.selenium.find_element(By.TAG_NAME, "body").text)
        # レビュー点数が100点を超えていたら投稿できないことを確認
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        score_input.send_keys('101')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("この値は 100 以下でなければなりません。", self.selenium.find_element(By.TAG_NAME, "body").text)
        # レビュー点数が自然数でないと投稿できないことを確認
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        score_input.send_keys('10.1')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # 既にユーザーが同名のゲームのレビューを投稿していたら、二重投稿できないことを確認
        # 一度、正規のデータで登録
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        score_input.send_keys('65')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post Success', self.selenium.title)
        # 再度同じゲームで登録できないことを確認
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[2]/div/a/strong")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Game Gallery', self.selenium.title)
        click_link = self.selenium.find_element(By.LINK_TEXT, "投稿する")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.send_keys('レビュータイトルテスト2')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.send_keys('レビューコメントテスト2')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.send_keys('99')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # エラーメッセージが表示されることを確認
        self.assertIn("以前レビューしたゲームは再度レビューはできません。", self.selenium.find_element(By.TAG_NAME, "body").text)
        print("バリデーションチェック：レビュー投稿処理　完了")   
 
    def test_review_pagenation(self):
        # テスト用に必要なオブジェクトを追加する
        for num in range(1, 20):
            Game.objects.create(title='テスト用ゲーム'+str(num), image1='../static/img/test.png')
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # 2ページ目に移動
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/ul/li[2]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # 文言チェック
        self.assertIn("テスト用ゲーム18", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム19", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム2", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム3", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム4", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム5", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム6", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム7", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム8", self.selenium.find_element(By.TAG_NAME, "body").text)
        # 次ページ(3ページ目)に移動
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/ul/li[5]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # 文言チェック
        self.assertIn("テスト用ゲーム9", self.selenium.find_element(By.TAG_NAME, "body").text)
        # 前ページ(2ページ目)に移動
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/ul/li[1]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # 文言チェック
        self.assertIn("テスト用ゲーム18", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム19", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム2", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム3", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム4", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム5", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム6", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム7", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム8", self.selenium.find_element(By.TAG_NAME, "body").text)
        print("正常テスト：ページネーション処理　完了")
    
    def test_detail(self):
        self.test_review_regist_success()
        # TOP画面へ遷移
        self.selenium.find_element(By.LINK_TEXT, "ゲームの評判").click()
        self.assertEquals('Game Gallery', self.selenium.title)
        # 投稿したレビューのディティール画面へ遷移
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/rect/div/div/div/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Game Detail', self.selenium.title)
        # 文言チェック
        self.assertIn("レビュータイトルテスト", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("レビューコメントテスト", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("65 点", self.selenium.find_element(By.TAG_NAME, "body").text)
        # ヘッダ画面からマイページへ遷移
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[2]/div/button/span")
        self.selenium.execute_script("arguments[0].click();", click_link)
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/ul/li[1]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Mypage', self.selenium.title)
        # 投稿したレビューのディティール画面へ遷移
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/rect/div/div/div/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Game Detail', self.selenium.title)
        # 文言チェック
        self.assertIn("レビュータイトルテスト", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("レビューコメントテスト", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("65 点", self.selenium.find_element(By.TAG_NAME, "body").text)
        print("正常テスト：ディティール画面表示処理　完了")
        
    def test_review_delete(self):
        self.test_detail()
        # レビュー削除画面に遷移
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertIn("削除してもよろしいですか？", self.selenium.find_element(By.TAG_NAME, "body").text)
        # 削除完了後、マイページ画面に遷移させる
        self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button").click()
        self.assertEquals('Mypage', self.selenium.title)
        self.assertIn("unittestさんの投稿はありません", self.selenium.find_element(By.TAG_NAME, "body").text)
        print("正常テスト：レビュー削除画面表示処理　完了")
        
    def test_logout(self):
        self.test_login_success()
        # ログアウト画面に遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "ログアウト")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Log out', self.selenium.title)
        print("正常テスト：ログアウト処理　完了")

    def test_password_reset_success(self):
        # TOPページを開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        # ログイン画面へ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "登録済みの方はログイン")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Log in', self.selenium.title)
        # パスワードリセット画面へ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "パスワードを忘れましたか？")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Reset password', self.selenium.title)
        # ダミーのメールアドレスを入力し、成功画面に遷移する
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys('unittest@test.com')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[3]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # リセットメール送信成功画面に遷移したことを確認する
        self.assertEquals('Send password reset', self.selenium.title)
        print("正常テスト：パスワードリセットメール送信処理　完了")
        
    def test_password_reset_failure(self):
        # TOPページを開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        # ログイン画面へ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "登録済みの方はログイン")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Log in', self.selenium.title)
        # パスワードリセット画面へ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "パスワードを忘れましたか？")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Reset password', self.selenium.title)
        # バリデーションチェック１：無入力
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[3]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Reset password', self.selenium.title)
        # バリデーションチェック２：@を含まない入力
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys('unittest')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[3]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Reset password', self.selenium.title)
        print("異常・バリデーションチェック：パスワードリセットメール送信処理　完了")
        
    def test_page_transition_header(self):
        ### ヘッダ画面の遷移テスト テストケース1-1
        ### 1-1-1~1-1-3はログアウト、1-1-4~1-1-7はログイン時のテスト
        # TOPページを開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        ## サインアップ画面へ遷移 テストケース1-1-1
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[2]/div/button/span")
        self.selenium.execute_script("arguments[0].click();", click_link)
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/ul/li[1]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Sign up', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## ログイン画面へ遷移 テストケース1-1-2
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/ul/li[2]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Log in', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## メール送信画面へ遷移は別途アプリが必要なので省略 テストケース1-1-3、1-1-7
        ## マイページ画面へ遷移 テストケース1-1-4
        # ログインが必要なので、一旦ログインする
        self.test_login_success()
        # TOPページを開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        # マイページリンクをクリック
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[2]/div/button/span")
        self.selenium.execute_script("arguments[0].click();", click_link)
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/ul/li[1]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Mypage', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## パスワードリセット画面へ遷移 テストケース1-1-6
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/ul/li[3]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Reset password', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## ログアウト画面へ遷移 テストケース1-1-5
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/ul/li[2]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Log out', self.selenium.title)
        print("画面遷移テスト：ページヘッダ部分　完了")
        
    def test_page_transition_top(self):
        ### TOP画面の遷移テスト テストケース1-2
        ### 1-2-1~1-2-4はログアウト、1-2-5~1-2-8はログイン時のテスト
        # ディティール画面用のデータを追加
        for num in range(1, 20):
            Game.objects.create(title='テスト用ゲーム'+str(num), image1='../static/img/test.png')
        # TOPページを開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        ## サインアップ画面へ遷移 テストケース1-2-1
        click_link = self.selenium.find_element(By.LINK_TEXT, "今すぐサインアップ")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Sign up', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## ログイン画面へ遷移 テストケース1-2-2
        click_link = self.selenium.find_element(By.LINK_TEXT, "登録済みの方はログイン")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Log in', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## ディティール画面へ遷移 テストケース1-2-3
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/rect/div/div/div/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Game Detail', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## ページネーション遷移 テストケース1-2-4
        # 2ページ目に移動
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/ul/li[2]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # 文言チェック
        self.assertIn("テスト用ゲーム18", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム19", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム2", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム3", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム4", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム5", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム6", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム7", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム8", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## レビュー登録画面へ遷移 テストケース1-2-5
        # ログインが必要なので、一旦ログインする
        self.test_login_success()
        # TOPページを開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        # 投稿ページへのリンクをクリック
        click_link = self.selenium.find_element(By.LINK_TEXT, "投稿する")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Post', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## ディテール画面へ遷移 テストケース1-2-7
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/rect/div/div/div/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Game Detail', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## ページネーション遷移 テストケース1-2-8
        # 2ページ目に移動
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/ul/li[2]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # 文言チェック
        self.assertIn("テスト用ゲーム18", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム19", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム2", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム3", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム4", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム5", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム6", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム7", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム8", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.selenium.back()
        self.assertEquals('Game Gallery', self.selenium.title)
        ## ログアウト画面へ遷移 テストケース1-2-6
        click_link = self.selenium.find_element(By.LINK_TEXT, "ログアウト")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Log out', self.selenium.title)
        print("画面遷移テスト：TOP画面　完了")
        
    def test_page_transition_detail(self):
        ### ディテール画面の遷移テスト テストケース1-3
        ## ログイン時のレビュー削除画面への遷移テスト テストケース1-3-2
        self.test_detail()
        # レビュー削除画面に遷移
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # 遷移したことを確認
        self.assertIn("削除してもよろしいですか？", self.selenium.find_element(By.TAG_NAME, "body").text)
        ## ログアウト時のレビュー削除画面へ遷移できないことを確認するテスト テストケース1-3-1
        # 一旦ログアウトする
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEquals('Game Gallery', self.selenium.title)
        click_link = self.selenium.find_element(By.LINK_TEXT, "ログアウト")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Log out', self.selenium.title)
        # TOP画面からディテール画面へ遷移する
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/rect/div/div/div/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Game Detail', self.selenium.title)
        # 削除ボタンが無い（削除できない）ことを確認
        self.assertNotIn("自分のレビューを削除する", self.selenium.find_element(By.TAG_NAME, "body").text)
        print("画面遷移テスト：ディテール画面　完了")
        
    def test_page_transition_signup(self):
        ### サインアップ画面の遷移テスト テストケース1-4
        # サインアップ画面を開く
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEquals('Game Gallery', self.selenium.title)
        click_link = self.selenium.find_element(By.LINK_TEXT, "今すぐサインアップ")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Sign up', self.selenium.title)
        ## TOP画面への遷移テスト テストケース1-4-1
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/p/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Sign up', self.selenium.title)
        ## サインアップ成功画面への遷移テスト テストケース1-4-2
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys('unittest')
        email_input = self.selenium.find_element(By.NAME, "email")
        email_input.send_keys('unittest@test.com')
        password1_input = self.selenium.find_element(By.NAME, "password1")
        password1_input.send_keys('Selenium2023')
        password2_input = self.selenium.find_element(By.NAME, "password2")
        password2_input.send_keys('Selenium2023')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/input[2]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Registration Complete', self.selenium.title)
        print("画面遷移テスト：サインアップ画面　完了")
        
    def test_page_transition_signup_success(self):
        ### サインアップ成功画面の遷移テスト テストケース1-5
        ## ログイン画面への遷移テスト テストケース1-5-1
        self.test_signup_success()
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/p[1]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Log in', self.selenium.title)
        print("画面遷移テスト：サインアップ成功画面　完了")
        
    def test_page_transition_login(self):
        ### ログイン画面の遷移テスト テストケース1-6
        self.test_signup_success()
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEquals('Game Gallery', self.selenium.title)
        click_link = self.selenium.find_element(By.LINK_TEXT, "登録済みの方はログイン")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Log in', self.selenium.title)
        ## パスワードリセット画面への遷移テスト テストケース1-6-1
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/form/p[1]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Reset password', self.selenium.title)
        self.selenium.back()
        self.assertEquals('Log in', self.selenium.title)
        ## ログイン画面（ログイン失敗時）への遷移テスト テストケース1-6-3
        # 不正なログイン情報を入れ、ログインできないことを検証
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys('test')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('test')
        self.selenium.find_element(By.CLASS_NAME, "btn").click()
        # ページタイトルの検証
        self.assertEquals('Log in', self.selenium.title)
        self.assertIn("ユーザ名とパスワードが一致しません", self.selenium.find_element(By.TAG_NAME, "body").text)
        ## TOP画面（ログイン成功時）への遷移テスト テストケース1-6-2
        # ログイン情報を入れ、ログインできないことを検証
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys('unittest')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys('Selenium2023')
        self.selenium.find_element(By.CLASS_NAME, "btn").click()
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        print("画面遷移テスト：ログイン画面　完了")
        
    def test_page_transition_review_regist(self):
        ### レビュー投稿画面の遷移テスト テストケース1-7
        ## レビュー投稿画面で内容不備で画面遷移しないことの確認 1-7-2
        # テスト用に必要なオブジェクトを追加する
        Game.objects.create(title='テスト用ゲーム', image1='../static/img/test.png')
        self.test_login_success()
        # レビュー投稿ページへ遷移
        click_link = self.selenium.find_element(By.LINK_TEXT, "投稿する")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        # 投稿できないレビュー情報を入れ、投稿ボタンを押下する
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.send_keys('-1')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # 遷移されていないことを確認
        self.assertEquals('Post', self.selenium.title)
        self.assertIn("この値は 0 以上でなければなりません。", self.selenium.find_element(By.TAG_NAME, "body").text)
        ## レビュー登録完了画面への遷移テスト テストケース1-7-1
        # レビュー情報を入れ、投稿ボタンを押下する
        game_input = self.selenium.find_element(By.NAME, "game")
        game_select = Select(game_input)
        game_select.select_by_index(1)
        title_input = self.selenium.find_element(By.NAME, "title")
        title_input.clear()
        title_input.send_keys('レビュータイトルテスト')
        comment_input = self.selenium.find_element(By.NAME, "comment")
        comment_input.clear()
        comment_input.send_keys('レビューコメントテスト')
        score_input = self.selenium.find_element(By.NAME, "score")
        score_input.clear()
        score_input.send_keys('65')
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post Success', self.selenium.title)
        print("画面遷移テスト：レビュー投稿画面　完了")
        
    def test_page_transition_review_delete(self):
        ### レビュー削除画面の遷移テスト テストケース1-9
        self.test_detail()
        # レビュー削除画面に遷移
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertIn("削除してもよろしいですか？", self.selenium.find_element(By.TAG_NAME, "body").text)
        ## ディティール画面への遷移テスト　テストケース1-9-2
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Game Detail', self.selenium.title)
        self.selenium.forward()
        ## マイページ画面への遷移テスト　テストケース1-9-1
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/form/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Mypage', self.selenium.title)
        print("画面遷移テスト：レビュー削除画面　完了")
        
    def test_page_transition_mypage(self):
        ### マイページ画面の遷移テスト テストケース1-10
        self.test_login_success()
        test_user = CustomUser.objects.get(username="unittest")
        # ディティール画面用のデータを追加
        for num in range(1, 20):
            test_game = Game.objects.create(title='テスト用ゲーム'+str(num), image1='../static/img/test.png')
            ReviewPost.objects.create(title="テストタイトル", user=test_user, game=test_game, comment="テストコメント", score="65")
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[2]/div/button/span")
        self.selenium.execute_script("arguments[0].click();", click_link)
        click_link = self.selenium.find_element(By.XPATH, "/html/body/header/div[1]/div/div/div[2]/ul/li[1]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Mypage', self.selenium.title)
        ## レビュー登録画面への遷移テスト テストケース1-10-1
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div[1]/a[1]")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Post', self.selenium.title)
        self.selenium.back()
        ## ディティール画面への遷移テスト テストケース1-10-3
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/div[1]/div/rect/div/div/div/button")
        self.selenium.execute_script("arguments[0].click();", click_link)
        self.assertEquals('Game Detail', self.selenium.title)
        self.selenium.back()
        ## ページネーション遷移 テストケース1-10-4
        # 2ページ目に移動
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/ul/li[2]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # 文言チェック
        self.assertIn("テスト用ゲーム10", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム11", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム12", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム13", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム14", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム15", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム16", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム17", self.selenium.find_element(By.TAG_NAME, "body").text)
        self.assertIn("テスト用ゲーム18", self.selenium.find_element(By.TAG_NAME, "body").text)
        ## ログアウト画面への遷移テスト テストケース1-10-2
        click_link = self.selenium.find_element(By.LINK_TEXT, "ログアウト")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Log out', self.selenium.title)
        print("画面遷移テスト：マイページ画面　完了")
        
    def test_page_transition_logout(self):
        ### ログアウト画面の遷移テスト テストケース1-11
        self.test_logout()
        ## TOP画面への遷移テスト テストケース1-11-1
        click_link = self.selenium.find_element(By.XPATH, "/html/body/main/div/div/div/p[1]/a")
        self.selenium.execute_script("arguments[0].click();", click_link)
        # ページタイトルの検証
        self.assertEquals('Game Gallery', self.selenium.title)
        print("画面遷移テスト：ログアウト画面　完了")
