import matplotlib.pyplot as plt
import set_file_name
import os

# create folder to store files in
def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

# This code will the traces and save them as a PDF
abf = set_file_name.abf
folder_name = set_file_name.folder
new_folder = create_folder(f"{folder_name}/new_{folder_name}")


for i in range(16):#list sweeps you want to see
    abf.setSweep(i)
    plt.plot(abf.sweepX, abf.sweepY, color="blue", alpha=.5, label=f"sweep {i}")
    plt.ylim(-80, 50)
    plt.xlim(0,1)
    i = i+1
    plt.savefig(f"{set_file_name.folder}/new_{folder_name}/{set_file_name.folder}0{set_file_name.file_number}_sweep{i}.pdf")
    plt.legend()
    plt.show()