#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

# @Time    : 2020/12/3 1:28
# @Author  : TNanko（开宝箱）
# @Site    : https://tnanko.github.io
# @File    : qq_read.py
# @Software: PyCharm
"""
此脚本使用 Python 语言根据 https://raw.githubusercontent.com/ziye12/JavaScript/master/Task/qqreads.js 改写
使用教程 https://github.com/TNanko/Scripts/blob/master/docs/qq_read.md
"""

import sys
import os
cur_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(cur_path)[0]
sys.path.append(root_path)
import json
import re
import time
import random
import requests
import traceback
from setup import get_standard_time
from utils import notify
from utils.configuration import read


def pretty_dict(dict):
    """
    格式化输出 json 或者 dict 格式的变量
    :param dict:
    :return:
    """
    return print(json.dumps(dict, indent=4, ensure_ascii=False))


def get_user_info(headers):
    """
    获取任务信息
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/user/init'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def get_daily_beans(headers):
    """
    阅豆签到
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/sign_in/user'
    try:
        response = requests.post(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def get_daily_tasks(headers):
    """
    获取今日任务列表
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/red_packet/user/page?fromGuid='
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            # print('获取今日任务')
            # pretty_dict(response['data'])
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def get_today_read_time(headers):
    """
    得到今日阅读时长
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/page/config?router=%2Fpages%2Fbook-read%2Findex&options='
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        # print('今日阅读')
        # pretty_dict(response)
        if response['code'] == 0:
            return response['data']['pageParams']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def read_time_reward_tasks(headers, seconds):
    """
    阅读奖励，好像一个号只能领一次
    :param headers:
    :param seconds:
    :return:
    """
    url = f'https://mqqapi.reader.qq.com/mqq/red_packet/user/read_time_reward?seconds={seconds}'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        # print('阅读奖励')
        # pretty_dict(response)
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def get_week_read_time(headers):
    """
    周阅读时长
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/v1/bookShelfInit'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        # print('周阅读时长')
        # pretty_dict(response)
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def read_now(headers):
    """
    立即阅读
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/red_packet/user/read_book'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        # pretty_dict(response)
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def read_tasks(headers, seconds):
    """
    每日阅读任务
    :param headers:
    :param seconds:
    :return:
    """
    url = f'https://mqqapi.reader.qq.com/mqq/red_packet/user/read_time?seconds={seconds}'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def daily_sign(headers):
    """
    今日打卡
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/red_packet/user/clock_in/page'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def watch_daily_sign_ads(headers):
    """
    今日打卡看广告翻倍
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/red_packet/user/clock_in_video'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        time.sleep(3)
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def watch_videos(headers):
    """
    看视频，拿金币
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/red_packet/user/watch_video'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def open_treasure_box(headers):
    """
    每20分钟开一次宝箱
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/red_packet/user/treasure_box'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        time.sleep(15)
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def watch_treasure_box_ads(headers):
    """
    看广告，宝箱奖励翻倍
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/red_packet/user/treasure_box_video'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        time.sleep(15)
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def get_week_read_tasks(headers):
    """
    周阅读奖励查询
    :param headers:
    :return:
    """
    url = 'https://mqqapi.reader.qq.com/mqq/pickPackageInit'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def get_week_read_reward(headers, read_time):
    """
    领取周阅读奖励
    :param headers:
    :param read_time: 阅读时长
    :return:
    """
    url = f'https://mqqapi.reader.qq.com/mqq/pickPackage?readTime={read_time}'
    try:
        response = requests.get(url=url, headers=headers, timeout=30).json()
        # print(f'领取周阅读奖励({read_time})')
        # pretty_dict(response)
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def read_books(headers, book_url, upload_time):
    """
    刷时长
    :param headers:
    :return:
    """
    try:
        upload_time_for_url = random.randint((upload_time - 1) * 60 * 1000, (upload_time + 1) * 60 * 1000)
        time_in_url = re.compile(r'readTime=(.*?)&read_')
        book_url = re.sub(time_in_url.findall(book_url)[0], str(upload_time_for_url), str(book_url))
        try:
            time_in_chapter_info = re.compile(r'readTime%22%3A(\d+)%2C')
            book_url = re.sub(time_in_chapter_info.findall(book_url)[0], str(upload_time_for_url), str(book_url))
        except:
            time_in_chapter_info = re.compile(r'"1":{"readTime":(\d+),"pay_status"')
            book_url = re.sub(time_in_chapter_info.findall(book_url)[0], str(upload_time_for_url), str(book_url))
        response = requests.get(url=book_url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return f'{upload_time_for_url // 1000 // 60}分{upload_time_for_url // 1000 % 60}秒'
        else:
            return
    except:
        print(traceback.format_exc())
        return


def track(headers, body):
    """
    数据追踪，解决1金币问题
    :param headers:
    :param body:
    :return:
    """
    try:
        url = 'https://mqqapi.reader.qq.com/log/v4/mqq/track'
        timestamp = re.compile(r'"dis": (.*?),')
        body = json.dumps(body)
        body = re.sub(timestamp.findall(body)[0], str(int(time.time() * 1000)), str(body))
        response = requests.post(url=url, headers=headers, data=body, timeout=30).json()
        if response['code'] == 0:
            return True
        else:
            return
    except:
        print(traceback.format_exc())
        return


def get_red_packets(headers, pn):
    """
    今日金币统计
    :param headers:
    :param pn: 金币列表序号
    :return:
    """
    try:
        url = f'https://mqqapi.reader.qq.com/mqq/red_packet/user/trans/list?pn={pn}'
        response = requests.get(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return response['data']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def get_withdraw_info(headers):
    try:
        url = 'https://mqqapi.reader.qq.com/mqq/red_packet/user/withdraw/page'
        response = requests.get(url=url, headers=headers, timeout=30).json()
        if response['code'] == 0:
            return response['data']['configList']
        else:
            return
    except:
        print(traceback.format_exc())
        return


def withdraw_to_wallet(headers, amount):
    try:
        url = f"https://mqqapi.reader.qq.com/mqq/red_packet/user/withdraw?amount={amount}"
        response = requests.post(url=url, headers=headers, timeout=30).json()
        if response['data']['code'] == 0:
            return True
        # 实名认证检测
        # elif response['data']['code'] == -300 and response['data']['msg'] == 'REALNAME_CHECK_ERROR':
        #     return f"{response['data']['msg']}，请前去QQ进行实名认证！"
        else:
            return response['data']['msg']
    except:
        print(traceback.format_exc())
        return '访问提现接口错误！'


def qq_read():
    config_latest, config_current = read()
    # 读取企鹅读书配置
    try:
        qq_read_config = config_current['jobs']['qq_read']
    except:
        print('配置文件中没有此任务！请更新您的配置文件')
        return
    # 脚本版本检测
    try:
        if qq_read_config['skip_check_script_version']:
            print('参数 skip_check_script_version = true ，跳过脚本版本检测...')
        elif config_latest:
            if config_latest['jobs']['qq_read']['version'] > qq_read_config['version']:
                print(f"检测到最新的脚本版本号为{config_latest['jobs']['qq_read']['version']}，当前脚本版本号：{qq_read_config['version']}")
            else:
                print('当前脚本为最新版本')
        else:
            print('未获取到最新脚本的版本号')
    except:
        print('程序运行异常，跳过脚本版本检测...')
    # 获取config.yml账号信息
    accounts = qq_read_config['parameters']['ACCOUNTS']
    # 每次上传的时间
    upload_time = qq_read_config['parameters']['UPLOAD_TIME']
    # 每天最大阅读时长
    max_read_time = qq_read_config['parameters']['MAX_READ_TIME']
    # 消息推送方式
    notify_mode = qq_read_config['notify_mode']

    # 确定脚本是否开启执行模式
    if qq_read_config['enable']:
        for account in accounts:
            try:
                book_url = account['BOOK_URL']
                headers = account['HEADERS']
                body = account['BODY']
                withdraw = account['WITHDRAW']
                hosting_mode = account['HOSTING_MODE']
                utc_datetime, beijing_datetime = get_standard_time()
                symbol = '=' * 16
                print(f'\n{symbol}【企鹅读书】{utc_datetime.strftime("%Y-%m-%d %H:%M:%S")}/{beijing_datetime.strftime("%Y-%m-%d %H:%M:%S")} {symbol}\n')

                start_time = time.time()
                title = f'☆【企鹅读书】{beijing_datetime.strftime("%Y-%m-%d %H:%M:%S")} ☆'
                content = ''
                # 调用 track 接口，为保证输出结果美观，输出信息写在后面
                track_result = track(headers=headers, body=body)
                # 获取用户信息（昵称）
                    for week_read_reward in week_read_rewards:
                        if not week_read_reward['isPick']:
                            reward = get_week_read_reward(headers=headers, read_time=week_read_reward['readTime'])
                            if reward:
                                content += f"\n【周时长奖励】领取{week_read_reward['readTime']}时长奖励成功"

                # 开宝箱领金币
                if daily_tasks['treasureBox']['doneFlag'] == 0:
                    treasure_box_reward = open_treasure_box(headers=headers)
                    if treasure_box_reward:
                        content += f"\n【开启第{treasure_box_reward['count']}个宝箱】获得{treasure_box_reward['amount']}金币"

                # 宝箱金币奖励翻倍
                daily_tasks = get_daily_tasks(headers=headers)
                                content += f'\n【满额提现】余额不足10元，未打开托管模式，不提现！'
                    else:
                        content += f'\n【自动提现】未到23点'
                else:
                    content += f'\n【自动提现】未启用该功能'

                content += f'\n🕛耗时：%.2f秒' % (time.time() - start_time)
                content += f'\n如果帮助到您可以点下🌟STAR鼓励我一下，谢谢~'
                print(title)
                print(content)
                # 每天 22:00 - 22:10 发送消息推送
                if qq_read_config['notify'] and beijing_datetime.hour == 22 and beijing_datetime.minute <= 10:
                    notify.send(title=title, content=content, notify_mode=notify_mode)
                elif not qq_read_config['notify']:
                    print('未进行消息推送，原因：未设置消息推送。如需发送消息推送，请确保配置文件的对应的脚本任务中，参数notify的值为true\n')
                elif not beijing_datetime.hour == 22:
                    print('未进行消息推送，原因：没到对应的推送时间点\n')
                else:
                    print('未在规定的时间范围内\n')

            except:
                headers = account['HEADERS']
                utc_datetime, beijing_datetime = get_standard_time()
                ywguid = re.match(r'ywguid=(.*?);', str(headers['Cookie']), re.I)
                if ywguid:
                    pattern = re.compile(r'\d+')
                    qq_id = pattern.findall(str(ywguid.group()))
                    print(f'☆【企鹅读书】{beijing_datetime.strftime("%Y-%m-%d %H:%M:%S")} ☆\nQQ账号 {qq_id[0]} headers过期!')
                    if qq_read_config['notify'] and beijing_datetime.hour / 3 == 0 and beijing_datetime.minute < 10:
                        notify.send(title=f'☆【企鹅读书】{beijing_datetime.strftime("%Y-%m-%d %H:%M:%S")} ☆',
                                    content=f'QQ账号 {qq_id[0]} headers过期!', notify_mode=notify_mode)
                else:
                    print('获取QQ账号失败，请检查headers')
    else:
        print('未执行该任务，如需执行请在配置文件的对应的任务中，将参数enable设置为true\n')


def main():
    qq_read()


if __name__ == '__main__':
    main()
