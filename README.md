**LANGUAGES** -------> | **English** | **[Español](README_ES.md)** |

![about](https://github.com/EliezerB03/DWI/assets/77678499/ff7474cd-bb68-483f-9805-0acbee04e209)

# Device Warehouse Inventory

[![Download](https://img.shields.io/badge/Download%20Here-v3.2-purple?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgAAAAIABAMAAAAGVsnJAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAFVBMVEUAAAAAeNQAd9UAd9MAeNQAeNT////IcS01AAAABXRSTlMAt5xvglcUpGIAAAABYktHRAZhZrh9AAAAB3RJTUUH6AcBDw0x03OxcAAAAmhJREFUeNrt2TERgEAQBMGjQABYQMFLwMT7t/LpFQjYgB4FW51uzVRntbbYjAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPgA3KlGB9hjM0qSJEmSJEmSJEl/6Ur19BVHbIZzFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4N0CjspD4koCRx4AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjQtMDctMDFUMTU6MTM6NDkrMDA6MDAPIJKnAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDI0LTA3LTAxVDE1OjEzOjQ5KzAwOjAwfn0qGwAAAABJRU5ErkJggg==&logoColor=blue)](https://github.com/EliezerB03/DWI/releases/latest)
[![LicensePSF2.0](https://img.shields.io/badge/License-PSF%202.0-green?style=for-the-badge&logo=python&logoColor=green)](https://docs.python.org/3/license.html#psf-license-agreement-for-python-release)
[![LicenseMIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwMCIgaGVpZ2h0PSIyNDIyIiB2aWV3Qm94PSIwIDAgMjU2IDI0OCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCI+PHBhdGggZD0iTTE0My4zMzcgMTY3LjgzMmMyMi4wNjMtOC40NzMgMzMuMDgyLTMzLjIzMSAyNC42MTItNTUuMzAxLTguNDctMjIuMDctMzMuMjIyLTMzLjA5Mi01NS4yODQtMjQuNjItMjIuMDYzIDguNDczLTMzLjA4MSAzMy4yMzItMjQuNjEyIDU1LjMwMmE0Mi43OTYgNDIuNzk2IDAgMCAwIDI0LjYxMiAyNC42MTlsLTI4LjgyMyA3NS4xM0MyMC4zIDIxOC41NjQtMTEuNDQgMTQ3LjI2IDEyLjk0OSA4My42OThjMjQuMzg5LTYzLjU2MiA5NS42Ny05NS4zMTEgMTU5LjIxMi03MC45MTUgNjMuNTQxIDI0LjM5NyA5NS4yODEgOTUuNyA3MC44OTIgMTU5LjI2MmExMjMuMjU0IDEyMy4yNTQgMCAwIDEtNzAuODkyIDcwLjkxNWwtMjguODI0LTc1LjEyOSIgZmlsbD0iIzNEQTYzOSIvPjxwYXRoIGQ9Ik0xNzIuMTYgMjQ3LjM2OWE0LjQwNCA0LjQwNCAwIDAgMS00LjExMy0yLjgyOGwtMjguODI0LTc1LjEzYTQuNDA4IDQuNDA4IDAgMCAxIDIuNTM1LTUuNjk0YzkuNTcxLTMuNjc1IDE3LjE0LTEwLjg2IDIxLjMxLTIwLjIzIDQuMTctOS4zNjkgNC40NDItMTkuODAyLjc2Ny0yOS4zNzYtNy41ODUtMTkuNzY2LTI5LjgzMS0yOS42NzMtNDkuNTktMjIuMDg1LTE5Ljc2IDcuNTg5LTI5LjY2NCAyOS44NDItMjIuMDc4IDQ5LjYwN2EzOC40NDYgMzguNDQ2IDAgMCAwIDIyLjA3NyAyMi4wODQgNC40MDggNC40MDggMCAwIDEgMi41MzUgNS42OTRsLTI4LjgyNCA3NS4xM2E0LjQwNiA0LjQwNiAwIDAgMS01LjY5MiAyLjUzNWMtMzEuODMtMTIuMjItNTYuOTk4LTM2LjExLTcwLjg2Ny02Ny4yNjYtMTMuODY4LTMxLjE1Ni0xNC43NzgtNjUuODUtMi41Ni05Ny42OUMyMS4wNTEgNTAuMjggNDQuOTMzIDI1LjEwNCA3Ni4wOCAxMS4yM2MzMS4xNDYtMTMuODczIDY1LjgyOS0xNC43ODMgOTcuNjYtMi41NjIgMzEuODMgMTIuMjIxIDU2Ljk5OCAzNi4xMSA3MC44NjYgNjcuMjY2IDEzLjg2OSAzMS4xNTYgMTQuNzc4IDY1Ljg1IDIuNTYgOTcuNjktMTIuOTQyIDMzLjczMi0zOS43MDYgNjAuNTA0LTczLjQyNyA3My40NTFhNC4zOTcgNC4zOTcgMCAwIDEtMS41NzguMjkzek0xMjcuOTU5IDguOTRjLTE2LjQzMyAwLTMyLjgzIDMuNDU2LTQ4LjI5NCAxMC4zNDNDNTAuNjcgMzIuMiAyOC40MzYgNTUuNjM3IDE3LjA2MyA4NS4yOGMtMTEuMzc0IDI5LjY0Mi0xMC41MjcgNjEuOTQgMi4zODQgOTAuOTQ1IDEyLjMxMiAyNy42NiAzNC4xODggNDkuMTY2IDYxLjg4OCA2MC45NjlsMjUuNzEyLTY3LjAyYTQ3LjI4NSA0Ny4yODUgMCAwIDEtMjMuMTA3LTI1LjM4Yy05LjMyNy0yNC4zMDQgMi44NS01MS42NjYgMjcuMTQ2LTYwLjk5NiAyNC4yOTctOS4zMyA1MS42NDkgMi44NTIgNjAuOTc2IDI3LjE1NCA0LjUxOSAxMS43NzMgNC4xODMgMjQuNjAyLS45NDQgMzYuMTIyLTQuNTI1IDEwLjE2OC0xMi4zMDUgMTguMjQzLTIyLjE2IDIzLjEwNmwyNS43MDggNjcuMDExYzI5LjQ2NS0xMi41OSA1Mi43NTEtMzYuNjk0IDY0LjI3NC02Ni43MjQgMTEuMzczLTI5LjY0MSAxMC41MjctNjEuOTQtMi4zODUtOTAuOTQ1LTEyLjkxLTI5LjAwNS0zNi4zNC01MS4yNDUtNjUuOTczLTYyLjYyMi0xMy44MzEtNS4zMS0yOC4yNDEtNy45NTgtNDIuNjI0LTcuOTU4ek0yMzcuNzQxIDIyOS41NzVjLTEuNTk3IDEuNjMzLTIuMzk1IDMuNTctMi4zOTUgNS44MTIgMCAyLjMyMi44MTIgNC4yOTYgMi40MzYgNS45MiAxLjYxNSAxLjYyNCAzLjU2NiAyLjQzNiA1Ljg1MyAyLjQzNiAyLjI3NyAwIDQuMjI0LS44MTYgNS44MzktMi40NSAxLjYxNS0xLjY0MiAyLjQyMi0zLjYxIDIuNDIyLTUuOTA2IDAtMi4yMzMtLjgwMy00LjE3LTIuNDA5LTUuODEyLTEuNjI0LTEuNjctMy41NzUtMi41MDUtNS44NTItMi41MDUtMi4zMDUgMC00LjI3LjgzNS01Ljg5NCAyLjUwNXptMTIuOTE3IDEzLjAxMmMtMS45NTEgMS44ODctNC4yOTIgMi44My03LjAyMyAyLjgzLTIuODIyIDAtNS4yLS45NjYtNy4xMzItMi44OTgtMS45MzMtMS45MzMtMi45LTQuMzEtMi45LTcuMTMyIDAtMi45MzEgMS4wNDQtNS4zNjggMy4xMzEtNy4zMSAxLjk2LTEuODE0IDQuMjYtMi43MjIgNi45LTIuNzIyIDIuNzY4IDAgNS4xMzIuOTggNy4wOTIgMi45NHMyLjk0IDQuMzI0IDIuOTQgNy4wOTJjMCAyLjg0OS0xLjAwMyA1LjI0OS0zLjAwOCA3LjJ6bS02LjExMS0xMC41NDljLS40LS4xNTQtLjk2Mi0uMjMxLTEuNjg4LS4yMzFoLS43MDh2My4yMjZoMS4xM2MuNjggMCAxLjIxMS0uMTM2IDEuNTkyLS40MDkuMzgxLS4yNzIuNTcyLS43MTIuNTcyLTEuMzIgMC0uNjA4LS4zLTEuMDMtLjg5OC0xLjI2NnptLTUuMzA5IDguOTI5di0xMS4xMmMuNjkgMCAxLjcyMi4wMDIgMy4wOTcuMDA3IDEuMzc1LjAwNCAyLjE0LjAxMSAyLjI5My4wMi44OC4wNjQgMS42MS4yNTQgMi4xOTIuNTcyLjk4OS41NDQgMS40ODMgMS40MjkgMS40ODMgMi42NTQgMCAuOTM1LS4yNiAxLjYxLS43ODIgMi4wMjgtLjUyMi40MTctMS4xNjQuNjY3LTEuOTI2Ljc0OS42OTguMTQ1IDEuMjI1LjM1OCAxLjU3OS42NC42NTMuNTI1Ljk4IDEuMzU2Ljk4IDIuNDl2Ljk5NGMwIC4xMDguMDA2LjIxNy4wMi4zMjYuMDE0LjExLjAzOC4yMTguMDc1LjMyN2wuMDk1LjMxM2gtMi43NzdjLS4wOS0uMzU0LS4xNS0uODY3LS4xNzYtMS41MzgtLjAyOC0uNjcyLS4wODctMS4xMjUtLjE3Ny0xLjM2MWExLjM0OCAxLjM0OCAwIDAgMC0uODE3LS44MTdjLS4yMTgtLjA5LS41NDktLjE1LS45OTQtLjE3N2wtLjY0LS4wNGgtLjYxMnYzLjkzM2gtMi45MTN6IiBmaWxsPSIjMUQ1MzFEIi8+PC9zdmc+Cg==&logoColor=white)](https://opensource.org/license/mit)
[![LicenseApache2.0](https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge&logo=apache&logoColor=green)](https://www.apache.org/licenses/LICENSE-2.0)

A Program that Facilitates the Management of Inventory Device Information from a Local Database.

### Main Features
- Add information to the Inventory with a Unique ID.
- Edit Inventory information using the ID as a reference.
- Delete information from the Inventory using the ID as a reference.
- Encrypted Account and Inventory Data.
- Inventory Import/Export System (in CSV File).
- Support for System/Light/Dark Themes.

### Languages Available
- English
- Spanish

### Requirements to Work
- Windows 10 x64 (Build 14393 on v2.3 or Higher) or Windows 8 x64 (Build 9200 on v2.2 or Below)
- Display Resolution: 1024 x 768 or Higher

### Requirements for some Features
- System Theme (Windows 10 Build 19042 or Higher)

### Licenses
- Some Built-In Python Modules and Tools used in this Project are Licensed under [PSF-2.0](https://docs.python.org/3/license.html#psf-license-agreement-for-python-release).
- Some Modules and Files used in this Project are Licensed under [MIT](https://opensource.org/license/mit).
- Some Modules and Tools used in this Project are Licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).