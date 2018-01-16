import sys
import re

### Set some variables
# Test data
DEBUG = 0
email_text_input = 'trial-pages.txt'
email_text_output = "trial-pages.emails_akio.txt"

### Define the function
def extract_email(input_file, output_file):
    final_output = []
    # Loop through the input_file
    
    print("=============Starting loop=============")
    input_handle = open(input_file)
    for each_line in input_handle:
        x = re.findall('\w+@\w+\.\w+', each_line)
        if x == []:
            final_output.append("None")
        else:
            final_output.append(x[0])
    if DEBUG == 1:
        print(final_output)
    else: pass
    
    print("=============Done with extraction=============")
    final_words = ""
    for i in final_output:
        final_words = final_words + i + "\n"
    with open(output_file, 'w') as f:
        f.write("{}".format(final_words[:-1]))
    print("=============Done writing the output=============")

### main()
if __name__ == "__main__":
    if DEBUG == 1:
        extract_email(email_text_input,email_text_output)
    elif DEBUG == 0:
        extract_email(sys.argv[1],sys.argv[2])