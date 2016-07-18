import luigi


class FileInput(luigi.ExternalTask):
    '''
    Define the input file for our job:
        The output method of this class defines
        the input file of the class in which FileInput is
        referenced in "requires"
    '''

    # Parameter definition: input file path
    input_path = luigi.Parameter()

    def output(self):
        '''
        As stated: the output method defines a path.
        If the FileInput  class is referenced in a
        "requires" method of another task class, the
        file can be used with the "input" method in that
        class.
        '''
        return luigi.LocalTarget(self.input_path)


class CountIt(luigi.Task):
    '''
    Counts the words from the input file and saves the
    output into another file.
    '''

    input_path = luigi.Parameter()

    def requires(self):
        '''
        Requires the output of the previously defined class.
        Can be used as input in this class.
        '''
        return FileInput(self.input_path)

    def output(self):
        '''
        count.txt is the output file of the job. In a more
        close-to-reality job you would specify a parameter for
        this instead of hardcoding it.
        '''
        return luigi.LocalTarget('count.txt')

    def run(self):
        '''
        This method opens the input file stream, counts the
        words, opens the output file stream and writes the number.
        '''
        word_count = 0
        with self.input().open('r') as ifp:
            for line in ifp:
                word_count += len(line.split(' '))
        with self.output().open('w') as ofp:
            ofp.write(unicode(word_count))

if __name__ == "__main__":
    luigi.run(main_task_cls=CountIt)
