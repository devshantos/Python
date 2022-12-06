'''import function
first_title_text = input("Write your first tagline: ")

first_paragraph = input("Write your description:")

second_title = 'House Makes'

second_paragraph= 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,'

article = function.wp_title(first_title_text)+function.wp_paragraph(first_paragraph)+function.wp_title(second_title)+function.wp_paragraph(second_paragraph)
print(article)

Shanto = input("Enter your name here: ")

same= article, Shanto

print(same)
'''

import mobile_template
article1= "Walton Primo R10 comes with 6.52 inches HD+ IPS screen. It has a full-view waterdrop notch design."
article2 = "The back camera is of triple 13+2+2 MP with PDAF, depth sensor, macro lens, LED flash, f/2.2 aperture etc."
article3 = "features and Full HD video recording. The front camera is of 8 MP. Primo R10 comes with 4850 mAh battery and 10W Fast Charging."
article4 = "It has 4 GB RAM, 1.8 GHz octa-core CPU and Mali-G52 GPU. It is powered by a 12 nm Unisoc Tiger T610 chipset. "
article5 = "The device comes with 64 GB internal storage and dedicated MicroSD slot. There is a side-mounted fingerprint sensor in this phone."


print(random.choice(article4))