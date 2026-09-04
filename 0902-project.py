#writing weekly report
for i in range(1,51):
    with open(str(i) + "week.txt", "w", encoding = "utf8") as report_file:
        report_file.write("-{}week weekly report-".format(i))
        report_file.write("\n Department \n Name : \n Summary : ")