from progress.bar import Bar

class ProgressBar(Bar):
    message = 'Loading'
#     fill = '#'
    fill = '█'
    suffix = '%(percent).1f%% | ETA: %(eta)ds'
