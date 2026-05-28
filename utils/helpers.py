#helper.py

def format_alert_message(target, open_ports):
    
    if not open_ports:
        return f" [BÁO CÁO AN TOÀN]\n Mục tiêu: `{target}`\n Không phát hiện cổng mở nguy hiểm nào."

    
    msg = f" [CẢNH BÁO KHẨN CẤP] \n"
    msg += f" Mục tiêu: `{target}`\n"
    msg += f" Phát hiện {len(open_ports)} cổng đang MỞ:\n"
    
    for port in open_ports:
        msg += f" ├  Port `{port}`\n"
        
    msg += f" Yêu cầu quản trị viên kiểm tra ngay!"
    
    return msg