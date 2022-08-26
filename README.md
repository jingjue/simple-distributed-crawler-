# simple-distributed-crawler

这是第四届青训营大数据基础班6806队的简易分布式爬虫系统。



## **技术选型**

分布式爬虫系统基于Python语言和Flask框架进行开发，基于Scrapy框架编写网络爬虫，并通过Scrapyd部署网络爬虫，借助Scrapy-Redis框架实现分布式数据收集，通过Docker实现容器化部署。



## 功能模块

分布式爬虫系统主要包含网络爬虫管理、主题网络爬虫、通用网络爬虫三个模块：

（1）网络爬虫管理

网络爬虫管理模块采用基于Redis缓存数据库的爬虫架构Scrapy-Redis。将原有爬虫队列使用Redis数据库改进，URL存、取、删、去重，都在Redis数据库里进行。通过Master-Slaver网络爬虫架构，实现分布式爬虫，可灵活调度任务，爬取海量数据。在Master端，利用Redis数据库，进行URL指纹判重，Request分配，以及数据存储。Slaver作为爬虫程序执行端，主要负责执行爬虫规则以爬取数据网页数据，并将爬取过程中新的Request提交到Master的Redis数据库中。网络爬虫管理模块的后端请求处理模块是爬虫前端可视化的数据提供者，是前端页面与各个功能模块沟通的桥梁。后端请求处理模块通过Flask框架实现，负责处理前端发送的请求，根据前端发送的请求调用分布式爬虫任务调度模块并将模块返回的数据通过JSON格式发送给前端用于展示。

（2）主题网络爬虫

针对某特定事件，将爬取目标定位在与主题相关的页面中，实现特定舆情事件的精确筛选与爬取。首先通过分词算法对舆情事件描述信息分词，根据切分出来的词在网页内容中出现的密度和相关性判断是否属于爬取事件，从而使爬虫在一个简单的初始主题描述条件下，能够以较高正确率抓取与某一特定主题内容相关的网页，为面向主题的数据分析准备数据资源。

（3）通用网络爬虫

通过深度优先爬取策略和广度优先爬取策略，实时采集全网多渠道的新闻资讯、涉军数据、社交媒体网站，涵盖中国新闻网、搜狐新闻、百度新闻、微博、微信、知乎、强国论坛、政治、经济、军事相关百度贴吧，党政媒体如人民网、以及境外新闻网站、社交媒体网站数据的爬取。深度优先网络爬虫从起始页开始，依次爬取每个链接，处理完这条线路之后转入下一个起始页，然后继续追踪。广度优先策略将新发现的链接直接插入到待抓取URL队列的末尾，网络爬虫先抓取起始页中的所有网页，然后在选择其中的一个链接网页，继续抓取在此网页中链接的所有网页，在数据爬取过程中，不断从Cookie管理器中取出Cookie，用于访问需要认证的网站。在爬取任务中采用深度与广度相结合的方式来实现抓取，优先考虑广度优先，对深度进行限制最大深度。



## 项目分工

| **团队成员** | **主要贡献**                                          |
| ------------ | ----------------------------------------------------- |
| 肖楷         | 负责前端可视化项目开发，文档撰写                      |
| 孙晨瑜       | 负责爬虫项目开发，web后端开发，文档撰写，演示视频录制 |
| 王振琦       | 负责爬虫项目开发，web后端开发，文档撰写，演示视频录制 |



## 总结与反思

- 反思：团队协作存在一些问题：部分队员划水失联，积极性不佳；团队比较松散，比较依赖个人自觉；制定的任务从时间、目的、责任人上均不清晰，导致预期任务无法完成。

- 总结：通过此次团队协作开发，我们对分布式爬虫系统的设计与组成有了更深一步的了解和认识。我有幸结识了优秀的队友，将自己所学应用到了实际开发中。