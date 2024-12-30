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
