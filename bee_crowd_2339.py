def suficient_paper():
    competitor,paper,paper_per_competitor = map(int,input().split())
    if (paper/paper_per_competitor) >= competitor:
        return True
    return False

def main():
    if suficient_paper():
        print("S")
    else:
        print("N")
if __name__ == "__main__":
    main()
