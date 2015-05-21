# GuestBook
inspired by [Python Professional Programming 2nd edition](http://www.amazon.co.jp/dp/479804315X/ref=pd_lpo_sbs_dp_ss_2?pf_rd_p=187205609&pf_rd_s=lpo-top-stripe&pf_rd_t=201&pf_rd_i=4798032948&pf_rd_m=AN1VRQENFRJN5&pf_rd_r=03ERSJ5YA99XWBMYKT6S)
### Requirements
  - python 2.7.6
  - virtualenv
  - pip

### How to Use
```sh
  $ git clone https://github.com/yhoshino11/GuestBook.git
  $ cd GuestBook/
  $ virtualenv .venv
  $ virtualenv .venv/bin/activate
  (.venv)$ pip install .
  (.venv)$ guestbook
  * Running on http://127.0.0.1:8000
  (.venv)$ deactivate # exit virtualenv
```

### Updating Packages
```sh
  (.venv)$ virtualenv --clear .venv
  (.venv)$ pip install -r requirements.txt
```

### Version
1.0.0
