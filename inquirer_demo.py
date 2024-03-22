from InquirerPy import inquirer
import asyncio

async def inquirerTest():
    # password = await inquirer.secret("请输入你的密码:").execute_async()
    # print(password)
    # name = await inquirer.text("请输入你的名字:").execute_async()
    # print(name)
    # male = await inquirer.select("请选择你的性别：", choices=['男', '女']).execute_async()
    # print(male)
    # choices = ["address1", "address2", "address3"]
    # #这种支持模糊匹配搜索的方式选择
    # select_sell_token = await inquirer.fuzzy(message="Enter token symbol or address you want to sell:", match_exact=True, choices=choices).execute_async()
    # print(select_sell_token)
    # number = await inquirer.number(message="Enter a number", float_allowed=True, max_allowed=1000, invalid_message="您输入的值不正确").execute_async()
    # print(number)

    hobbit = await inquirer.checkbox("请勾选你的爱好", ["打球", "看电影", "听音乐"]).execute_async()
    print(hobbit)

if __name__ == '__main__':
    asyncio.run(inquirerTest())