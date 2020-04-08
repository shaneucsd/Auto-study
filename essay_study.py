from auto_study import auto_study

if __name__ == '__main__':

    '''
    实现自动上课
    '''
    slc = auto_study()
    slc.login(False)
    slc.study(course_name='经贸研究与论文写作-2-谢红军', course_time_by_minute=90)
    slc.quit()