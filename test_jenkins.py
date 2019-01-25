import allure
class TestJenkins:
	
	@allure.step(title="test01")
    def test01(self):
        print("test01")
        assert True
	@allure.step(title="test02")
    def test02(self):
        print("test02")
        assert False