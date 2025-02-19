import os
import soundfile as sf

def convert_wav_to_flac(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.lower().endswith('.wav'):
            input_path = os.path.join(input_directory, filename)
            
            output_filename = os.path.splitext(filename)[0] + '.flac'
            output_path = os.path.join(output_directory, output_filename)
            
            try:
                audio, samplerate = sf.read(input_path)
                sf.write(output_path, audio, samplerate, format='FLAC')
                print(f"변환 완료: {filename} -> {output_filename}")
            except Exception as e:
                print(f"변환 오류 ({filename}): {e}")

if __name__ == "__main__":
    input_directory = '' # wav 데이터 경로
    output_directory = '' # 생성된 flac 데이터 저장 경로

    convert_wav_to_flac(input_directory, output_directory)

    print("WAV에서 FLAC으로 변환 완료!")

