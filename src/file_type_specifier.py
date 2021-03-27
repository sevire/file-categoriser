file_categories = {
    'audio': {
        '.aif',
        '.cda',
        '.mid',
        '.midi',
        '.mp3',
        '.mpa',
        '.ogg',
        '.wav',
        '.wma',
        '.wpl',
        '.m3u',
    },
    'text': {
        '.txt',
        '.doc',
        '.docx',
        '.odt',
        '.pdf',
        '.rtf',
        '.tex',
        '.wks ',
        '.wps',
        '.wpd',
        '.opml',
        '.oo3',
        '.outline',
    },
    'email': {
        '.pst',
        '.mbx',
        '.dbx',
        ''
    },
    'video': {
        '.3g2',
        '.3gp',
        '.avi',
        '.flv',
        '.h264',
        '.m4v',
        '.mkv',
        '.mov',
        '.mp4',
        '.mpg',
        '.mpeg',
        '.rm',
        '.swf',
        '.vob',
        '.wmv',
        '.dv',
        '.ts',
    },
    'images': {
        '.ai',
        '.bmp',
        '.gif',
        '.jpg',
        '.jpeg',
        '.png',
        '.ps',
        '.psd',
        '.svg',
        '.tif',
        '.tiff',
        '.cr2',
    },
    'internet': {
        '.asp',
        '.aspx',
        '.cer',
        '.cfm',
        '.cgi',
        '.pl',
        '.css',
        '.scss',
        '.less',
        '.htm',
        '.js',
        '.jsp',
        '.part',
        '.php',
        '.rss',
        '.xhtml',
        '.html',
    },
    'compressed': {
        '.7z',
        '.arj',
        '.deb',
        '.pkg',
        '.rar',
        '.rpm',
        '.tar.gz',
        '.z',
        '.zip',
    },
    'disc': {
        '.bin',
        '.dmg',
        '.iso',
        '.toast',
        '.vcd',
        '.sparsebundle',
    },
    'data': {
        '.csv',
        '.dat',
        '.db',
        '.dbf',
        '.log',
        '.mdb',
        '.sav',
        '.sql',
        '.tar',
        '.xml',
        '.json',
    },
    'executables': {
        '.apk',
        '.bat',
        '.com',
        '.exe',
        '.gadget',
        '.jar',
        '.wsf',
    },
    'fonts': {
        '.fnt',
        '.fon',
        '.otf',
        '.ttf',
        '.woff2',
        '.woff',
        '.eot',
    },
    'presentations': {
        '.key',
        '.odp',
        '.pps',
        '.ppt',
        '.pptx',
    },
    'programming': {
        '.c',
        '.class',
        '.java',
        '.py',
        '.sh',
        '.h',
    },
    'spreadsheets': {
        '.numbers',
        '.ods',
        '.xlr',
        '.xls',
        '.xlsx',
    },
    'project': {
        '.mpp',
    },
    'system': {
        '.bak',
        '.cab',
        '.cfg',
        '.cpl',
        '.cur',
        '.dll',
        '.dmp',
        '.drv',
        '.icns',
        '.ico',
        '.ini',
        '.lnk',
        '.msi',
        '.sys',
        '.tmp',
    }
}


class FileCategory:
    def __init__(self, categories):
        self.file_categories = categories

    def get_file_category(self, suffix):  # Suffix includes the dot
        for category in self.file_categories:
            for cat_extension in self.file_categories[category]:
                if cat_extension == suffix:
                    return category
        return None

