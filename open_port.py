import miniupnpc
import sys

def create_port_map():
    upnp = miniupnpc.UPnP()
    upnp.discoverdelay = 200
    
    try:
        print("--- Huawei/Honor Port Opener ---")
        upnp.discover()
        upnp.selectigd()
        
        # اطلب من المستخدم إدخال IP الهاتف والمنفذ
        phone_ip = input("أدخل عنوان IP هاتف الهواوي: ")
        port = int(input("أدخل رقم المنفذ المراد فتحه: "))
        
        # تنفيذ العملية
        result = upnp.addportmapping(port, 'TCP', phone_ip, port, 'HonorPhoneForward', '')
        
        if result:
            print(f"\n✅ تم بنجاح! المنفذ {port} موجه الآن إلى {phone_ip}")
            print(f"IP الإنترنت الخارجي: {upnp.externalipaddress()}")
            
    except Exception as e:
        print(f"\n❌ حدث خطأ: {e}")
    
    input("\nاضغط Enter للخروج...")

if __name__ == "__main__":
    create_port_map()
