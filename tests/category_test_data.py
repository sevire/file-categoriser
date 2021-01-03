category_test_data_01 = {
    'categories': {
        'image': {
            'jpg',
            'jpeg',
            'png',
            'tiff',
            'gif',
            'bmp',
        },
        'video': {
            'mov',
            'mp4',
            'wmv',
            'mpeg',
        },
        'edge': {
            '',
            None
        }
    },
    'expected_results': [
        ('jpg', 'image'),
        ('jpeg', 'image'),
        ('png', 'image'),
        ('tiff', 'image'),
        ('gif', 'image'),
        ('bmp', 'image'),
        ('mov', 'video'),
        ('mp4', 'video'),
        ('wmv', 'video'),
        ('mpeg', 'video'),
        ('xxx', None),
        ('', 'edge'),
        (None, 'edge'),
    ]
}
