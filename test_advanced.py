import readline
import logging

LOG_FILENAME = '/tmp/completer.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )


class BufferAwareCompleter(object):

    def __init__(self, options):
        self.options = options         # commands to be completed
        self.current_candidates = []
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list.

            origline = readline.get_line_buffer()   # linebuffer
            begin    = readline.get_begidx()        # linebuffer begain id
            end      = readline.get_endidx()       :Q # linebuffer end id
            being_completed = origline[begin:end]   # being completed string
            words    = origline.split()

            logging.debug('origline=%s', repr(origline))
            logging.debug('begin=%s', begin)
            logging.debug('end=%s', end)
            logging.debug('being_completed=%s', being_completed)
            logging.debug('words=%s', words)

            if not words:
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if begin == 0:
                        # first word
                        candidates = self.options.keys()
                    else:
                        # later word
                        first = words[0]
                        candidates = self.options[first]

                    if being_completed:
                        # match options with portion of input
                        # being completed
                        self.current_candidates = [w for w in candidates
                                                   if w.startswith(being_completed)]
                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates

                    logging.debug('candidates=%s', self.current_candidates)

                except (KeyError, IndexError):
                    logging.error('completion error: %s', err)
                    self.current_candidates = []

        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s', repr(text), state, response)
        return response


def input_loop():
    line = ''
    while line != 'stop':
        line = input('Prompt ("stop" to quit): ')
        print
        'Dispatch %s' % line


# Register our completer function
readline.set_completer(BufferAwareCompleter(
    {'list': ['files', 'directories'],
     'print': ['byname', 'bysize'],
     'stop': [],
     }
).complete)

# Use the tab key for completion
readline.parse_and_bind('tab: complete')

# Prompt the user for text
input_loop()