import glob, csv
import matplotlib.pyplot as plt

def read_data(filename):
    files = glob.glob(filename)
    all_data = []
    for file in files:
        with open(file, 'r') as f:     # Construct a file object
            csv_reader = csv.reader(f) # Construct a CSV reader object
            data = []
            for line in csv_reader:
                if line and not line[0].strip().startswith('#'): # If 'line' is valid and not a header
                    data.append([int(val) for val in line])      # Append 'line' to 'data' as numbers
            all_data = all_data + data                           # Merge 'data' to 'all_data'
    return all_data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # Derive miterm, final, and total scores
    midtm_kr = [row[0]for row in class_kr]
    final_kr = [row[1]for row in class_kr]
    total_kr = [row[0]*40/125+row[1]*60/100 for row in class_kr]
    midtm_en = [row[0]for row in class_en]
    final_en = [row[1]for row in class_en]
    total_en = [row[0]*40/125+row[1]*60/100 for row in class_en]

    # Plot midterm/final scores as points
    plt.figure(figsize=(5,10))
    plt.subplot(2,1,1)
    plt.plot(midtm_kr, final_kr,'r*',label='Korean')
    plt.title(" KOREA midterm/final scores as points")
    plt.legend(loc='best')
    plt.ylabel('FinalTerm')
    plt.grid()
    plt.subplot(2,1,2)
    plt.plot(midtm_en, final_en,'g^',label='English')
    plt.title("ENGLISH midterm/final scores as points")
    plt.xlabel(' Midterm')
    plt.ylabel('FinalTerm')
    plt.legend(loc='best')
    plt.suptitle("scores as points")
    plt.grid()
    plt.savefig('class_score_scatter.png')
    # Plot total scores as a histogram
    
    # Plot total scores as a histogram
    plt.figure()
    plt.hist(total_kr,range=(0,100),bins=20,color='r',histtype='bar',density=True,cumulative=True,label="total_kr")
    plt.hist(total_en,range=(0,100),bins=20,alpha=0.5,color='c',histtype='bar',density=True,cumulative=True,label='total_en',)
    plt.title('TOTAL TERM')
    plt.xlabel('SCORE POINT MAX =100')
    plt.legend()
    plt.show()
    
    