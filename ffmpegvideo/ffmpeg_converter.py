import subprocess


class FFMPEG_Converter:
    def convert_webm_mp4_subprocess(self, input_file, output_file):
        try:
            input_f = r'{}'.format(input_file)
            output_f = r'{}'.format(output_file)
            command = 'ffmpeg -fflags +genpts -loglevel quiet -i "{}" -r 60 "{}"'.format(input_f, output_f)
            subprocess.run(command)
            print("transformation done!")
        except:
            print("Subprocess Failed Converting")

