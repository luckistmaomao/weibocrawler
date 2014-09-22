#coding:utf-8
import traceback

import sys

reload(sys)
sys.setdefaultencoding('utf8')  # @UndefinedVariable

try:
    from weibo_scheduler import get_weibo_scheduler
    from keyword_processor import get_keyword_processor
    from weibo_branch import get_user_keyword_processor
    from get_valid_ip import proxy_ip_manager
    from common_conf_manager import OPEN_PROXY_CRAWL
    
    import logging
    import logging.config
except ImportError as err:
    s = traceback.format_exc()
    
    print s
    
logging.config.fileConfig('runtime_infor_log.conf')

scheduler_logger = logging.getLogger("schedulerLog")
def main():
    
    threads = []
    
    user_keyword_pro = get_user_keyword_processor()
    threads.append(user_keyword_pro)
    
    keyword_pro = get_keyword_processor()
    threads.append(keyword_pro)
    
    weibo_scheduler = get_weibo_scheduler()
    threads.append(weibo_scheduler)
    
    if OPEN_PROXY_CRAWL:
        threads.append(proxy_ip_manager)
    
    for thread in threads:
        scheduler_logger.info("thread " + thread.name + " start!")
        thread.start()
    
    for thread in threads:
        thread.join()
        
if __name__ == '__main__':
    
    main()
