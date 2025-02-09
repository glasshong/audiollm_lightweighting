# 오디오 언어모델의 경량 모델링 레서피 탐구

## 🥇 팀 구성원

<div align="center">
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/kupulau">
        <img src="https://github.com/user-attachments/assets/d78bb2d1-6469-43e4-9665-eca058f1a2e5" width="120px" height="120px" alt=""/>
        <hr />
        <sub><b>황지은</b></sub><br />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/asotea">
        <img src="https://github.com/user-attachments/assets/a15d120c-f086-4f3c-8902-25dd260675ba" width="120px" height="120px" alt=""/>
        <hr />
        <sub><b>김태균</b></sub><br />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/mujjinungae">
        <img src="https://github.com/user-attachments/assets/9098f35a-2002-4f6c-ba66-e3a94310a9f5" width="120px" height="120px" alt=""/>
        <hr />
        <sub><b>이진우</b></sub><br />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/glasshong">
        <img src="https://github.com/user-attachments/assets/5474a1fb-63ca-465e-b85e-0689beb35d87" width="120px" height="120px" alt=""/>
        <hr />
        <sub><b>홍유리</b></sub><br />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/EuiInSeong">
        <img src="https://github.com/user-attachments/assets/6e33239b-6101-4d5d-807a-2a01a7f39cc7" width="120px" height="120px" alt=""/>
        <hr />
        <sub><b>성의인</b></sub><br />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/jinbong-yeom">
        <img src="https://github.com/user-attachments/assets/73fd05b7-0884-46c8-8b4a-fb787626138c" width="120px" height="120px" alt=""/>
        <hr />
        <sub><b>염진봉</b></sub><br />
      </a>
    </td>
  </tr>
</table>
</div>

<br />

## 🗒️ 프로젝트 개요

"Audio adapter의 결합 및 사전학습을 통해, 언어모델은 음성/음악/환경음 등의 소리를 이해하고 다양한 downstream task를 수행할 수 있게 되었습니다. VRAM의 크기가 작은 전형적인 디바이스 환경에서는 오디오 언어모델에 대한 경량 모델링이 필수적입니다. Audio understanding benchmarks에 대한 baseline 모델의 정확도를 유지하면서도, 더 작고 빠른 모델을 만드는 레서피를 디자인해 주시기를 기대합니다."

해당 프로젝트는 네이버 부스트캠프 AI Tech 7기 기업 해커톤으로 kaggle에서 진행됩니다.

- ASR 평가 : https://www.kaggle.com/competitions/boostcamp-7th-nota-hackathon
- AAC 평가 : https://www.kaggle.com/competitions/boostcamp-7th-nota-hackathon-aac

<br />

## 📅 프로젝트 일정

프로젝트 전체 일정

- 2025.01.10 (금) ~ 2025.02.12 (수)

프로젝트 세부 일정

![schedule](https://github.com/user-attachments/assets/2d351923-4b2c-4a2b-ab01-5a78a0e96aee)

## 💻 개발 환경

```bash
- Language : Python
- Environment
  - CPU : Intel(R) Xeon(R) Gold 5120
  - GPU : Tesla V100-SXM2-32GB x 2
- Framework : PyTorch
- Collaborative Tool : Git, Wandb, Notion
```

## 📁 데이터셋 구조

```
📦 data
├── 📂 audiocaps
│   ├── 📂 test
│   └── 📂 train
├── 📂 Clotho
│   └── 📂 train
├── 📂 GigaSpeech
│   ├── 📂 0
│   ├── 📂 1
│   ├── 📂 10
...
│   └── 📂 9
├── 📂 LibriSpeech
│   ├── 📂 test-other
│   ├── 📂 train-clean-100
│   ├── 📂 train-clean-360
│   └── 📂 train-other-500
├── 📂 MusicNet
│   └── 📂 train
└── 📂 WavCaps
    ├── 📂 AudioSet_SL
    ├── 📂 BBC_Sound_Effects
    ├── 📂 FreeSound
    └── 📂 SoundBible
```

- 학습에 사용하는 오디오 파일은 1,609,722개, 추론에 사용하는 오디오 파일은 7,294개 저장되어 있습니다. 
- 제공되는 오디오 파일은 wav, flac 형식으로 된 speech, non-speech sound로 구성되어 있습니다.
- json 파일은 각 오디오 파일에 대한 Automatic Speech Recognition, Automatic Audio Captioning 등의 annotation 내용이 포함되어 있습니다.

<br />

## 📁 프로젝트 구조 

```
📦level4-cv-finalproject-hackathon-cv-03-lv3
├── 📂 audiolm-evaluator
│   ├── 📂 audiolm-trainer
│   ├── 📂 data
│   ├── 📜 evaluate_efficiency_salmonn.py
│   ├── 📜 evaluate_salmonn.py
│   ├── 📜 metrics.py
│   ├── 📜 README.md
│   ├── 📜 requirements.txt
│   ├── 📜 salmonn_eval_config.yaml
│   ├── 📜 salmonn_utils.py
│   ├── 📂 submission_results
│   └── 📜 submission_validator.py
├── 📜 BEATs_iter3_plus_AS2M_finetuned_on_AS2M_cpt2.pt
├── 📂 boostcamp-7th-nota-hackathon
│   ├── 📜 stage1_test.json
│   ├── 📜 stage1_train.json
│   ├── 📜 stage2_test.json
│   ├── 📜 stage2_train.json
│   ├── 📜 test_aac.json
│   └── 📜 test_asr.json
├── 📂 EDA
│   ├── 📜 EDA2.ipynb
│   ├── 📜 EDA.ipynb
│   ├── 📜 QA_fill.ipynb
│   ├── 📜 stage1_train.csv
│   ├── 📜 stage2_train.csv
│   ├── 📜 Taegyun.ipynb
│   ├── 📜 test_aac.csv
│   └── 📜 test_asr.csv
└── 📜 salmonn_3b_nota.pth
```

<br />

## ⚙️ requirements

- torch==2.5.1
- torchaudio==2.5.1
- peft==0.3.0
- soundfile==0.12.1
- librosa==0.10.2.post1
- transformers==4.47.1
- sentencepiece==0.1.97
- accelerate==1.2.1
- bitsandbytes==0.45.0
- gradio==3.23.0
- wandb==0.19.1
- omegaconf==2.3.0
- tensorboardX==2.6.2.2
- editdistance==0.8.1
- sacrebleu==1.5.1
- aac-metrics==0.5.4

`pip install -r requirements.txt`

<br />

## ▶️ 실행 방법

#### 학습 및 체크포인트 저장

`python train.py --cfg-path config.yaml`

#### 추론

`python evaluate_salmonn.py --mode {submission_aac, submission_asr, valid_aac, valid_asr}`

<br />