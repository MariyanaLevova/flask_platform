from systeminfo import main as sysinfo

@app.route('/)
def get_system_info():
    return "The platform is "+ sysinfo.get_platform_info()

