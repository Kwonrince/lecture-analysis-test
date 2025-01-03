from datetime import datetime, timedelta

class TimeConverter:
    """
    시간 변환과 관련된 유틸리티 클래스.
    """
    @staticmethod
    def convert_time_to_milliseconds(time_str):
        """
        "Xm Ys" 형식의 시간을 밀리초(ms) 단위로 변환.
        """
        minutes, seconds = 0, 0
        if 'm' in time_str:
            minutes = int(time_str.split('m')[0].strip())
            seconds = float(time_str.split('m')[1].replace('s', '').strip())
        elif 's' in time_str:
            seconds = float(time_str.replace('s', '').strip())
        return int((minutes * 60 + seconds) * 1000)  # ms 단위로 변환
    
    def convert_timerange_to_milliseconds(time_str):
        """
        "Xm Ys ~ X'm Y's" 형식의 시간을 밀리초(ms) 단위로 변환.
        """
        time_str = time_str.split(' ~ ')
        time_list = []
        for time in time_str:
            minutes, seconds = 0, 0
            if 'm' in time:
                minutes = int(time.split('m')[0].strip())
                seconds = float(time.split('m')[1].replace('s', '').strip())
            elif 's' in time:
                seconds = float(time.replace('s', '').strip())
            time_list.append(int((minutes * 60 + seconds) * 1000))
        return time_list

    @staticmethod
    def format_ms_to_ktc(ms):
        """
        밀리초(ms)를 KTC 시간 표현(YYYY-MM-DD HH:mm:ss.sss)으로 변환.
        """
        base_time = datetime(1970, 1, 1) + timedelta(milliseconds=ms)
        return base_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]

    @staticmethod
    def format_ms_to_xm_ys(ms):
        """
        밀리초(ms)를 Xm Ys 형태로 변환.
        """
        total_seconds = ms / 1000
        minutes = int(total_seconds // 60)
        seconds = total_seconds % 60
        return '{:01d}m {:.1f}s'.format(minutes, seconds)

    @staticmethod
    def format_ms_to_xm_ys_range(ms_list):
        """
        밀리초(ms)를 "Xm Ys ~ X'm Y's" 형태로 변환.
        """
        minutes = []
        seconds = []
        for ms in ms_list:
            total_seconds = ms / 1000
            minutes.append(int(total_seconds // 60))
            seconds.append(total_seconds % 60)
        return '{:01d}m {:.1f}s'.format(minutes[0], seconds[0]) + " ~ " + '{:01d}m {:.1f}s'.format(minutes[1], seconds[1])