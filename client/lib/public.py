class shared_module:
    #以下是整个程序
    app=None
    #以下是ui的实例化对象
    login_page=None
    main_page=None
    reg_page=None
    setip_page=None
    add_friend=None
    new_friends=None
    progress_bar=None
    new_group=None
    manage_group=None
    video_page=None
    #以下是功能实例化对象
    client=None 
    #以下是线程实例化对象
    file_thread = None
    listen_thread=None
    video_thread = None

    #以下是调试参数
    full_fuction=True
    FileSendThread_signal = None