import billboard

def main():
    hot100 = billboard.ChartData('hot-100')
    # billboard.ChartData('hot-100', date=None, fetch=True, max_retries=5, timeout=25)

    print("Billboard hot-100 chart from " + hot100.date + "\n---------------------------------------")
    for song in hot100:
        print(vars(song))
    
if __name__ == '__main__':
    main()

