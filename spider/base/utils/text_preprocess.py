#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @Author 冬兽
    @Date 2021/10/3 11:10
    @Describe 文本预处理
"""
import json
import logging
import re

from scrapy import Selector


def text_pre(text):
    """

    """
    return text.strip().replace("\u200b", "")


def people_pre_text(text):
    """
    人民网文本预处理，去除换行和头尾空格
    """
    return text.strip()


def mweibo_extract_script(text):
    """
    从mweibo中提取script，并返回json
    :param text:
    :return:
    """
    try:
        script = re.search("\$render_data = \[(.*)\] \[0\] \|\| \{\};", text).group(1)
        info_json = json.dumps(script)
        return info_json
    except:
        logging.exception(f"【html页面解析出错】 {text}")
        return None


def mweibo_xpath_content(text):
    """
    "【深圳女子<a  href=\"https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E5%9B%9B%E5%8D%83%E5%A4%9A%E4%B8%87%E4%B9%B0%E8%B1%AA%E5%AE%85%E6%80%80%E7%96%91%E8%A2%AB%E5%90%83%E5%B7%AE%E4%BB%B7250%E4%B8%87%23&extparam=%23%E5%9B%9B%E5%8D%83%E5%A4%9A%E4%B8%87%E4%B9%B0%E8%B1%AA%E5%AE%85%E6%80%80%E7%96%91%E8%A2%AB%E5%90%83%E5%B7%AE%E4%BB%B7250%E4%B8%87%23&luicode=20000061&lfid=4690818105608683\" data-hide=\"\"><span class=\"surl-text\">#四千多万买豪宅怀疑被吃差价250万#</span></a>，<a  href=\"https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E4%B8%AD%E4%BB%8B%E5%9B%9E%E5%BA%94%E5%A5%B3%E5%AD%90%E4%B9%B0%E8%B1%AA%E5%AE%85%E8%A2%AB%E5%90%83%E5%B7%AE%E4%BB%B7250%E4%B8%87%23&extparam=%23%E4%B8%AD%E4%BB%8B%E5%9B%9E%E5%BA%94%E5%A5%B3%E5%AD%90%E4%B9%B0%E8%B1%AA%E5%AE%85%E8%A2%AB%E5%90%83%E5%B7%AE%E4%BB%B7250%E4%B8%87%23&luicode=20000061&lfid=4690818105608683\" data-hide=\"\"><span class=\"surl-text\">#中介回应女子买豪宅被吃差价250万#</span></a>：经内部调查，只收了合法佣金，办理人员已离职<span class=\"url-icon\"><img alt=[傻眼] src=\"https://h5.sinaimg.cn/m/emoticon/icon/default/d_shayan-4e8000eba9.png\" style=\"width:1em; height:1em;\" /></span>】近日，深圳一市民夏女士（化名）向南都记者反映称，她在2020年底购买一套房产，中介工作人员帮她争取为4150万元成交价格，并支付33.2万元中介佣金费，于2021年1月办理相关手续。夏女士经过邻居提醒价格过高，因此询问前业主后得知其挂牌价为3800万元，但最终实际收了3900万元，有250万元的费用由中介收取。<br /><br />10月9日，记者联系前业主张女士，其回应称该套房产的售卖价格为3900万元，其中产生的佣金差价不知被谁收取。记者联系了中原地产代理（深圳）有限公司，工作人员回应称，经公司内部调查，除合法佣金以外并未收取夏女士任何费用。并明确约定买卖双方实际应承担的佣金数额，双方无信息差。据悉，当时服务夏女士的中介工作人员目前已从中原地产代理（深圳）有限公司离职。<br /><br />广东大匠律师事务所主任、律师刘小前认为，根据《民法典》相关规定，如果中介方收取了佣金差价，夏女士不仅可以要求中介退还佣金，并且可以要求中介承担夏女士所遭受的损失。刘小前表示，夏女士在中介拒绝退还佣金的情况下，可通过充分举证后，向法院提起诉讼，维护自身的合法权益。（南方都市报·深圳大件事）<a  href=\"https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E8%8A%B14150%E4%B8%87%E4%B9%B0%E6%88%BF%E7%96%91%E8%A2%AB%E4%B8%AD%E4%BB%8B%E8%B5%9A250%E4%B8%87%E5%B7%AE%E4%BB%B7%23&extparam=%23%E8%8A%B14150%E4%B8%87%E4%B9%B0%E6%88%BF%E7%96%91%E8%A2%AB%E4%B8%AD%E4%BB%8B%E8%B5%9A250%E4%B8%87%E5%B7%AE%E4%BB%B7%23&luicode=20000061&lfid=4690818105608683\" data-hide=\"\"><span class=\"surl-text\">#花4150万买房疑被中介赚250万差价#</span></a>",

    :param text:
    :return: 提取中文内容
    """
    info = Selector(text=text).xpath("string(.)").get()
    return info


def ifeng_extract_script(text):
    """
    从ifeng中提取script，并返回json
    :param text:
    :return:
    """

    try:
        script = re.search("var allData = (.*);", text).group(1)
        script = re.sub("<img (.*?)/>", "", script).replace("\u0009", "")

        info_json = json.loads(script)
        return info_json
    except:
        logging.exception(f"【html页面解析出错】 {text}")
        return None


if __name__ == '__main__':
    text = 'var allData = {"noffhFlag":["215401-","5-95384-","1-35220-","31-","275799-"],"headKeyword":["这条最新发布的内容，80%的网友都在看","热热热！这条精彩内容，你的朋友们都在看","过去24小时发生了这些好玩的事，点击查看","全网最热新闻出炉，这些事儿你都知道吗？","想不到！今天最火爆的新闻居然是……","这条重磅新闻刚刚发布！快来查看","过去的24小时你错过了这些重要新闻……","今天这条消息，90%的人都不知道！"],"searchPathData":[],"channelListData":[{"searchPath":"1-","title":"财经"},{"searchPath":"2-","title":"时尚"},{"searchPath":"3-","title":"资讯"},{"searchPath":"4-","title":"娱乐"},{"searchPath":"5-","title":"科技"},{"searchPath":"6-","title":"房产"},{"searchPath":"10-","title":"汽车"},{"searchPath":"11-","title":"体育"},{"searchPath":"12-","title":"健康"},{"searchPath":"14-","title":"军事"},{"searchPath":"15-","title":"历史"},{"searchPath":"16-","title":"佛教"},{"searchPath":"17-","title":"文化读书"},{"searchPath":"18-","title":"教育"},{"searchPath":"19-","title":"创新"},{"searchPath":"20-","title":"国学"},{"searchPath":"21-","title":"评论"},{"searchPath":"22-","title":"政务"},{"searchPath":"23-","title":"国际智库"},{"searchPath":"26-","title":"音乐"},{"searchPath":"27-","title":"视频"},{"searchPath":"28-","title":"公益"},{"searchPath":"29-","title":"酒业"},{"searchPath":"31-","title":"商业"},{"searchPath":"32-","title":"家居"},{"searchPath":"33-","title":"旅游"},{"searchPath":"95013-","title":"美食"},{"searchPath":"95379-","title":"小说"},{"searchPath":"215401-","title":"区域"},{"searchPath":"245409-","title":"文创"},{"searchPath":"245539-","title":"青春BANG"},{"searchPath":"275736-","title":"凤凰卫视"},{"searchPath":"275799-","title":"知之"}],"unfold":{"articleUnfold":"2","articleShareUnfold":"1","stopReadArticle":[],"videoShareUnfold":"1","topicPopup":"1","articleShareUnfoldLayer":{},"videoShareUnfoldLayer":{},"articleUnfoldLayer":{},"topicPopupLayer":{},"hotNewsBreakLayer":{},"wxGuideLayer":{"leaveSet":0,"startTime":"00:00:00","endTime":"23:59:59","continueBtnSet":0,"openSet":0,"switch":"2"},"browserGuideLayer":{"xiaomi":"2","ifengHome":"2","leaveSet":1,"chrome":"2","safari":"2","baidu":"2","continueBtnSet":1,"openSet":1,"uc":"2","addDay":0,"huawei":"2","ifengArticle":"2","oppo":"2","startTime":"00:00:00","vivo":"2","endTime":"23:59:59"},"wxLaunch":{"wxLaunchType":"1","wxLaunchSwitch":"1"},"regionFold":{"regionBlacklist":[{"province":"北京"},{"province":"广东"}],"startTime":"08:00:00","endTime":"18:59:59","switch":"2"}},"fixedIcon":{"image":"https://x0.ifengimg.com/ucms/2021_11/90DBBE0AF68ECC1E2BE3FE2EE38AE46F1679EFEA_size52_w300_h300.png","link":"https://ishare.ifeng.com/c/s/8480lNfRPbE?webkit=1","clientLink":"https://ishare.ifeng.com/c/s/8480lNfRPbE?webkit=1","topic":"4","video":"4","article":"4","bottomSlide":{"slideSwitch":"0","picUrl":"https://x0.ifengimg.com/ucms/2021_24/33058AECF6E405193151AA6A351D9D43772BD9EE_size18_w564_h112.jpg","gotoUrl":"https://ishare.iclient.ifeng.com/askacitve?webkit=1"}},"bigPicSwiperData":[],"wutongData":[{"id":0,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/ScsLrwZA3fBlbt690_gugw","title":"德国“双立人”指甲刀，剪指甲又快又安全，小机关让碎甲不乱飞 \t","source":"","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_31/3CF00F0BAD7EA11D9575C06180C318ABB86BB5B4_size20_w480_h270.jpg\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FScsLrwZA3fBlbt690_gugw"}}},{"id":1,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/HMCdsNq_UQaQ6HjV2DRtiw","title":"鼻塞流涕/干燥鼻痒？英国“鼻炎克星”连打鼾也好了 \t","source":"","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_33/BA387F8E6712A22D7131808A5CB322DED221C98C_size28_w640_h360.jpg\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FHMCdsNq_UQaQ6HjV2DRtiw"}}},{"id":2,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/ahFVsYYsPR3OaY4rBv_giw","title":"最懂国人肠胃的益生菌，每天一包，轻松调理肠胃，养出好肤色 \t","source":"","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_33/7F72F0F5585086C9CA09812D131274EF7CBA4E20_size72_w650_h366.jpg\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FahFVsYYsPR3OaY4rBv_giw"}}},{"id":3,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/pWSKpVbgwGtgP55PHrOVzQ","title":"口中常有“腐臭味”？根源在于这里 \t","source":"","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_33/6E317474212F66532FCBF65D8593FF12994A234B_size41_w543_h305.jpg\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FpWSKpVbgwGtgP55PHrOVzQ"}}},{"id":4,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/I5_4g6HpVO7rWwqG0wA9KA","title":"79元入手大马士革钢五件刀具，一秒断骨离筋，切肉像切黄瓜 \t","source":"","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_25/22BAD5E8150AD637EBE275631742C8B7299C9E04_size1248_w500_h281.gif\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FI5_4g6HpVO7rWwqG0wA9KA"}}},{"id":5,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/6jXyYO4mckKX06RNM67gjw","title":"海蓝之谜“贵妇水”仅4.3折，皮肤的安心水，努力跑过岁月的影响\t","source":"推广","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_33/E96849193699B874B21E710A1011271EF14179C2_size70_w650_h366.jpg\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F6jXyYO4mckKX06RNM67gjw"}}},{"id":6,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/7zTEK8kPqWUhc6B1sSBlng","title":"有了这款靠垫和坐垫，连坐8小时都不伤腰，还能美臀护腿 \t","source":"推广","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_33/A2EC2A4F96F07574B696C5D1DEF3FB0E53693DC4_size38_w650_h366.jpg\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F7zTEK8kPqWUhc6B1sSBlng"}}},{"id":7,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/JlX_0e91pnLvhjOK0Jyl2w","title":"这套中国历史书，比看90%电视剧有用处 \t","source":"推广","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_33/D48D0195BBD2BE7822332F4C7E6E21D4017C0739_size61_w650_h366.jpg\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FJlX_0e91pnLvhjOK0Jyl2w"}}},{"id":8,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/Mpqx6vnnp0ngqasnxPwIww","title":"日系搓澡巾，无痛搓泥！轻轻搓一搓，让全身舒爽\t","source":"推广","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_33/05FCE8DF81DBE617F7121F9112D3ABE09F33ED0C_size75_w640_h360.jpg\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FMpqx6vnnp0ngqasnxPwIww"}}},{"id":9,"type":"doc","newstype":"doc","url":"https://mp.weixin.qq.com/s/9AEGuSHthh41gezRlrSuwQ","title":"这个男人，写透了人性的爱与欲 \t","source":"推广","thumbnails":{"image":[{"bytes":277,"url":"https://x0.ifengimg.com/ucms/2021_33/EC403E8A978C4D17EA94BE103AC0C61AE22ADE2F_size103_w650_h366.gif\t"}]},"clickCount":{"behavior":"action","type":"click","other":{"rnum":0,"tag":"t7","kind":"article","url":"https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F9AEGuSHthh41gezRlrSuwQ"}}}],"removeAdArticle":["7ykAdqHhnU0"],"lianghuiId":{"data":["6776049327413404591","6775288060658585961","6775710911312175992","6775683997914632967","6775394446537134134"],"timestamp":"2021-03-12 18:00:00"},"activityOne":[],"activityTwo":[],"pageBottomPic":{"newBrandPic":"","schemeUrl":"type=bottomNav&navId=bottomNavVideo&id=vch_phoenix&kind=inter_dsjzt04","videoBrandPic":""},"lianghuiData":[{"id":"6776049327413404591","type":"article","url":"https://news.ifeng.com/c/84YNQIHXvOp","title":"两会闭幕后，这3位省级党委书记为何没立刻离京？","base62Id":"84YNQIHXvOp","thumbnail":"//d.ifengimg.com/w224_h150_q90/x0.ifengimg.com/ucms/2021_11/D660EB8DA16B6F8CC1F835E90A846FA3BB9B4FFE_size57_w650_h366.jpg"},{"id":"6775288060658585961","type":"short","url":"https://news.ifeng.com/c/84UtFlXRNd3","title":"凤凰专访王毅记者会提到的法国作家：没想到他会认识我","base62Id":"84UtFlXRNd3","thumbnail":"//d.ifengimg.com/w224_h150_q90/x0.ifengimg.com/ucms/2021_11/C4FE39DDBB12A0E6F251AE1A39F4F9321CA9FDC9_size164_w391_h220.png"}],"docData":{"_id":"v002i5cHTVKU3vi9rf1mvpxo3NTweU--wYVc2ceL3wS79E0U__","noffhFlag":false,"type":"article","status":1,"searchPath":"","title":"快手：捐赠1000万元驰援山西抗汛救灾，上线山西暴雨专题页","newsTime":"10/11 19:05","source":"","faceUrl":"//ishare.ifeng.com/mediaShare/home/645972/media","sourceUrl":"","summary":"快手：捐赠1000万元驰援山西抗汛救灾，上线山西暴雨专题页","shareSummary":"IT之家 10 月 11 日消息 据快手官方公众号，快手宣布捐赠 1000 万元驰援山西抗汛救灾。此外，快手还上线了山西暴雨专题页，第一时间发布灾情最新消息和救...","imagesInContent":[{"size":57,"width":719,"url":"https://x0.ifengimg.com/res/2021/D4FC3C35438D2E19F4068FCE89D593E447C05594_size57_w719_h347.png","height":347},{"size":431,"width":649,"url":"https://x0.ifengimg.com/res/2021/70372A7CFA6633C1442CDDCB7C80E4E3C6908831_size431_w649_h427.png","height":427}],"id":"6853274486326694467","base62Id":"8AG4KWUMFBj","pcUrl":"https://i.ifeng.com/c/8AG4KWUMFBj","url":"//i.ifeng.com/c/8AG4KWUMFBj","commentUrl":"ucms_8AG4KWUMFBj","skey":"ba6cee","wemediaEAccountId":"645972","slideData":[],"contentData":{"contentList":[{"data":"\u003cp>IT之家 10 月 11 日消息 据快手官方公众号，快手宣布捐赠 1000 万元驰援山西抗汛救灾。\u003c/p>\u003cp>此外，快手还上线了山西暴雨专题页，第一时间发布灾情最新消息和救助信息。\u003c/p>\u003cp>\u003cimg src=\"https://x0.ifengimg.com/res/2021/D4FC3C35438D2E19F4068FCE89D593E447C05594_size57_w719_h347.png\" />\u003c/p>\u003cp>\u003cstrong>快手公告原文：\u003c/strong>\u003c/p>\u003cp>近期，山西省遭遇极端异常的大范围持续降雨，导致严重洪涝灾害。汛情牵动人心，快手宣布向灾区捐赠 1000 万元人民币，用于紧急救助和灾后重建，并将持续密切关注汛情动态，携手各方共助灾区渡过难关。\u003c/p>\u003cp>与此同时，快手上线了山西暴雨专题页，第一时间发布灾情最新消息和救助信息，集合社会各界力量、最大化调动资源，为受灾地区和民众提供帮助。\u003c/p>\u003cp>山西加油，我们同在！\u003c/p>\u003cp>\u003cimg  class=\"empty_bg\" data-lazyload=\"https://x0.ifengimg.com/res/2021/70372A7CFA6633C1442CDDCB7C80E4E3C6908831_size431_w649_h427.png\" src=\"data:image/gif;base64,R0lGODlhAQABAIAAAP\" style=\"background-color:#f2f2f2;padding-top:65.79352850539291%;\"  />\u003c/p>\u003cp>IT之家了解到，进入 10 月以来，山西部分地区出现极端强降雨天气，并引发山洪和地质灾害，给当地人民生命与财产安全造成威胁。洪涝灾害已致山西全省 11 个市 76 个县（市、区）175.71 万人受灾，12.01 万人紧急转移安置，284.96 万亩农作物受灾，1.7 万余间房屋倒塌。\u003c/p>","type":"text"}],"currentPage":0,"pageSize":1},"editorName":"任福涛","thumbnails":{"image":[{"width":635,"url":"https://x0.ifengimg.com/ucms/2021_42/18DB35E9831525C3854FC82F60548D9D90914E91_size16_w635_h357.jpg","height":357}]},"vestAccountDetail":{"eAccountId":645972,"weMediaName":"","logo":"//d.ifengimg.com/w60_h60_q90/img1.ugc.ifeng.com/newugc/20171013/16/wemedia/dd29bf11fb682beaa7f0e7fcfcbc35a33b27ec93_size7_w200_h200.png","description":"有人的地方，就有江湖；有电脑手机平板的地方，就有IT之家。","honorName":"","honorImg":"http://p0.ifengimg.com/a/2018/0929/8c6f0f95dd440aesize5_w54_h54.png","accountStatus":1,"sourceFrom":"IT之家","behavioralControl":{"edit_aggregation":2,"algorithm_vote":2,"miniVideo":1,"content_mark":1,"edit_move":2,"icon":2,"video":1,"click":1,"article":1,"edit_add":1,"attention":1,"logo":1,"short":1,"mix":1}},"isVideoShare":false,"subscribe":{"type":"vampire","cateSource":"","isShowSign":0,"parentid":"0","parentname":"数码","cateid":"645972","catename":"IT之家","logo":"http://d.ifengimg.com/q100/img1.ugc.ifeng.com/newugc/20171013/16/wemedia/dd29bf11fb682beaa7f0e7fcfcbc35a33b27ec93_size7_w200_h200.png","description":"优质数码领域创作者","api":"http://api.3g.ifeng.com/api_wemedia_list?cid=645972","show_link":1,"share_url":"https://share.iclient.ifeng.com/share_zmt_home?tag=home&cid=645972","eAccountId":645972,"status":1,"honorName":"","honorImg":"http://x0.ifengimg.com/cmpp/2020/0907/1a8b50ea7b17cb0size3_w42_h42.png","honorImg_night":"http://x0.ifengimg.com/cmpp/2020/0907/b803b8509474e6asize3_w42_h42.png","forbidFollow":0,"forbidJump":0,"fhtId":"89973602","view":1,"sourceFrom":"","declare":"","originalName":"","redirectTab":"article","authorUrl":"https://ishare.ifeng.com/mediaShare/home/645972/media","newsTime":"2021-10-11 19:05:51"},"relatedRecommend":[]},"keywords":"山西,快手,专题,灾情,山西暴雨,灾区,洪涝灾害,暴雨","safeLevel":0,"isCloseAlgRec":false,"__env__":"production"};'

    print(ifeng_extract_script(text))
