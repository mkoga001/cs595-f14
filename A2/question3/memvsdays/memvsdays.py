import sys

def main():
    mementoData = {}
    ageData = {}

    mem_urls = open('mementos.txt','r')

    for line in mem_urls:
        line = line.strip()
        (mementoCount, uri) = line.split('\t')

        if int(mementoCount) > 0:
            mementoData[uri] = mementoCount

    mem_urls.close()

    carbon_date = open('cDays.txt','r')

    for line in carbon_date:
        line = line.strip()
        (age, uri) = line.split(' ')

        ageData[uri] = age

    carbon_date.close()
    for key in mementoData:
        print(key + ' ' + mementoData[key] + ' ' + ageData[key])
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
