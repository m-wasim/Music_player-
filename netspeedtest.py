import speedtest
test=speedtest.Speedtest()
download=test.download()
print(download)