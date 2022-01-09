import os
from natsort import natsorted

# path to the directory you want turned into a website
root = r"D:\Documents\Архив"
# path to the output folder
output_folder = r"D:\Documents\Programming\output"
# in order for the website to work, the output folder has to contain the directory you want visualised
# copy the "assets" folder into the output folder
def get_icon(entry):
    file = '<i class="bi bi-file-earmark"></i>\n'

    film = '<i class="bi bi-film"></i>\n'
    music = '<i class="bi bi-music-note-beamed"></i>\n'
    pdf = '<i class="bi bi-file-earmark-pdf"></i>\n'
    txt = '<i class="bi bi-file-earmark-text"></i>\n'
    word = '<i class="bi bi-file-earmark-word"></i>\n'
    image = '<i class="bi bi-image"></i>\n'
    archive = '<i class="bi bi-archive"></i>\n'
    spreadsheet = '<i class="bi bi-file-earmark-spreadsheet"></i>\n'
    email = '<i class="bi bi-envelope"></i>\n'
    database = '<i class="bi bi-server"></i>\n'
    book = '<i class="bi bi-book"></i>\n'
    executable = '<i class="bi bi-file-earmark-binary"></i>\n'

    film_extension = ['3g2', '3gp', 'avi', 'flv', 'h256', 'm4v', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'rm', 'swfw', 'vob', 'wmv']
    music_extension = ['mp3', 'wav', 'aif', 'wproj', 'ec3', 'weba', 'flp', 'abc', 'ckb', 'sdt', 'cgrp', 'nbs', 'flac', 'l', 'mui', 'ogg', 'cda', 'mid', 'midi', 'wma', 'mpa', 'wpl']
    pdf_extension = ['pdf']
    txt_extension = ['txt', 'tex']
    word_extension = ['doc', 'docx', 'odt', 'wpd']
    image_extension = ['ai', 'bmp', 'gif', 'ico', 'jpeg', 'jpg', 'png', 'ps', 'psd', 'svg', 'tif', 'tiff']
    archive_extension = ['7z', 'z', 'rpm', 'rar', 'pkg', 'deb', 'arj', 'zip']
    spreadsheet_extension = ['xlsx', 'xls', 'xlsm', '123', 'gnumeric', 'nb', 'dex', 'def', 'xl']
    email_extension = ['email', 'eml', 'emlx', 'msg', 'oft', 'ost', 'pst', 'vcf']
    database_extension = ['cvs', 'dat', 'db', 'dbf', 'log', 'mdb', 'sav', 'sql', 'tar', 'xml']
    book_extension = ['epub', 'fb2', 'ibook']
    executable_extension = ['apk', 'bat', 'cgi', 'pl', 'com', 'exe', 'gadget', 'jar', 'msi']

    extension_dict = dict.fromkeys(film_extension, film)
    extension_dict.update(dict.fromkeys(music_extension, music))
    extension_dict.update(dict.fromkeys(pdf_extension, pdf))
    extension_dict.update(dict.fromkeys(txt_extension, txt))
    extension_dict.update(dict.fromkeys(word_extension, word))
    extension_dict.update(dict.fromkeys(image_extension, image))
    extension_dict.update(dict.fromkeys(archive_extension, archive))
    extension_dict.update(dict.fromkeys(spreadsheet_extension, spreadsheet))
    extension_dict.update(dict.fromkeys(email_extension, email))
    extension_dict.update(dict.fromkeys(database_extension, database))
    extension_dict.update(dict.fromkeys(book_extension, book))
    extension_dict.update(dict.fromkeys(executable_extension, executable))
    return extension_dict.get(entry.split('.')[-1], file)


def get_features(items, dir_name):
    first = '<div class="col-lg-3 col-md-4"> \n                    <div class="icon-box"> \n                        '
    second = '<div class="col-lg-3 col-md-4 mt-4 mt-md-0"> \n                    <div class="icon-box"> \n                        '
    third = second
    fourth = ' <div class="col-lg-3 col-md-4 mt-4 mt-lg-0"> \n                    <div class="icon-box"> \n                        '
    following = '<div class="col-lg-3 col-md-4 mt-4"> \n                    <div class="icon-box"> \n                        '
    folder = '<i class="bi bi-folder"></i>'
    features = ''
    for i in range(len(items)):
        link = os.path.join(dir_name, items[i]).replace(root.replace(root.split('\\')[-1], ''), '')
        if i == 0:
            if os.path.isdir(os.path.join(dir_name, items[i])):
                features += first
                features = features + folder + ' \n                        <h3><a href=\"' + items[i] + '/' + items[i] + '.html\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n   \n                '

            else:
                features += first
                features += get_icon(items[i]) + ' \n                        <h3><a href=\"\\' + link + '\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n  '

        elif i == 1:
            if os.path.isdir(os.path.join(dir_name, items[i])):
                features += second
                features = features + folder + ' \n                        <h3><a href=\"' + items[i] + '/' + items[i] + '.html\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n   \n                '

            else:
                features += second
                features += get_icon(items[i]) + ' \n                        <h3><a href=\"\\' + link + '\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n  '

        elif i == 2:
            if os.path.isdir(os.path.join(dir_name, items[i])):
                features += third
                features = features + folder + ' \n                        <h3><a href=\"' + items[i] + '/' + items[i] + '.html\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n   \n                '

            else:
                features += third
                features += get_icon(items[i]) + ' \n                        <h3><a href=\"\\' + link + '\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n  '

        elif i == 3:
            if os.path.isdir(os.path.join(dir_name, items[i])):
                features += fourth
                features = features + folder + ' \n                        <h3><a href=\"' + items[i] + '/' + items[i] + '.html\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n   \n                '

            else:
                features += fourth
                features += get_icon(items[i]) + ' \n                        <h3><a href=\"\\' + link + '\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n  '

        else:
            if os.path.isdir(os.path.join(dir_name, items[i])):
                features += following
                features = features + folder + ' \n                        <h3><a href=\"' + items[i] + '/' + items[i] + '.html\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n   \n                '

            else:
                features += following
                features += get_icon(items[i]) + ' \n                        <h3><a href=\"\\' + link + '\">' + items[i] + '</a></h3> \n                    </div> \n                </div> \n  '


    return features


def get_header(header, dir_name):
    icon = '</a><i class="bi bi-caret-right-fill"></i><a href="'
    header = header + '<p><a href="'
    header = header + '../' * (dir_name.count('\\') - root.count('\\')) + dir_name.split('\\')[root.count('\\')] + '.html">' + dir_name.split('\\')[root.count('\\')]
    print(dir_name)
    for count in range(root.count('\\')+1, len(dir_name.split('\\'))):
        i = dir_name.split('\\')[count]
        header = header + icon + '../' * (dir_name.count('\\') - count) + i + '.html">' + i
    return header + '</a></p> \n            </div> \n        </div> \n    </section> \n    <section class="features mt-4"> \n        <div class="container" data-aos="fade-up"> \n   \n            <div class="row" data-aos="zoom-in" data-aos-delay="100"> \n   \n                '


def builder(dir_name, output_dir):
    contents = os.listdir(dir_name)
    list_of_dirs = ''
    list_of_files = ''
    header = '<!DOCTYPE html> \n<html lang="en"> \n \n<head> \n  <meta charset="utf-8"> \n  <meta content="width=device-width, initial-scale=1.0" name="viewport"> \n \n  <title>Archive</title> \n  <meta content="" name="description"> \n  <meta content="" name="keywords"> \n \n  <!-- Favicons --> \n  <link sizes="480x480" type="image/png" href="/assets/img/favicon.png" rel="icon"> \n  <link sizes="480x480" type="image/png" href="/assets/img/favicon.png" rel="shortcut icon"> \n  <link href="/assets/img/apple-touch-icon.png" rel="apple-touch-icon"> \n \n  <!-- Google Fonts --> \n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> \n  <!-- Vendor CSS Files --> \n  <link href="/assets/vendor/animate.css/animate.min.css" rel="stylesheet"> \n  <link href="/assets/vendor/aos/aos.css" rel="stylesheet"> \n  <link href="/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet"> \n  <link href="/assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet"> \n  <link href="/assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet"> \n  <link href="/assets/vendor/remixicon/remixicon.css" rel="stylesheet"> \n  <link href="/assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet"> \n \n  <!-- Template Main CSS File --> \n  <link href="/assets/css/style.css" rel="stylesheet"> \n <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n \n</head> \n \n<body> \n  <main id="main"> \n    <section> \n        <div class="container position-relative" data-aos="zoom-in" data-aos-delay="100"> \n            <div class="section-title"> \n                <h2> <a href="javascript:history.back()" class="btn-get-started"><i class="bi bi-arrow-left"></i>Назад</a></h2> \n                '
    footer = '</div> \n   \n        </div> \n    </section> \n  </main><!-- End #main --> \n   \n   \n   \n  <!-- Vendor JS Files --> \n  <script src="/assets/vendor/aos/aos.js"></script> \n  <script src="/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script> \n  <script src="/assets/vendor/php-email-form/validate.js"></script> \n  <script src="/assets/vendor/purecounter/purecounter.js"></script> \n  <script src="/assets/vendor/swiper/swiper-bundle.min.js"></script> \n \n  <!-- Template Main JS File --> \n  <script src="/assets/js/main.js"></script> \n<script> \n    $(".icon-box").click(function() { \n        window.location = $(this).find("a").attr("href");  \n        return false; \n    }); \n  </script> \n   \n</body> \n \n</html>'

    dirs = []
    files = []

    for entry in contents:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            dirs.append(entry)
            list_of_dirs += entry
            list_of_dirs += 'that is a folder \n'
            os.mkdir(os.path.join(output_dir, entry))
            builder(full_path, os.path.join(output_dir, entry))
        else:
            files.append(entry)
            list_of_files += entry
            list_of_files += 'file\n'
    dirs = natsorted(dirs)
    files = natsorted(files)
    header = get_header(header, dir_name)
    items = dirs + files
    features = get_features(items, dir_name)
    html_name = os.path.join(output_dir, os.path.basename(dir_name) + '.html')
    file1 = open(html_name, 'w', encoding='utf-8')

    to_file = header + features + footer
    file1.write(to_file)
    file1.close()


def main():
    builder(root, output_folder)


if __name__ == '__main__':
    main()