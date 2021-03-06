# Trolley

A tool for managing official Slackware packages, designed for unRAID.

Compatible with unRAID >5.0

## Install

With curl

    curl -skL http://git.io/8GviJQ | sh

With wget

    wget -qO- --no-check-certificate http://git.io/8GviJQ | sh -

You may need to reopen your terminal session after installing.

## Why use trolley?

### You need to install dependencies for a plugin

Without trolley: search the web for a package, download it, get it on your unRAID box, install it, and remember to put it in /boot/extra for next time.

With trolley, you can do all that in one go: `trolley install openssl`.

### You need to remove a broken or incompatible package

The common process is to remove it from /boot/extra then run removepkg. You might even have to restart.

With trolley, it's just `trolley remove openssl`. No restart required.

### You need to update existing dependencies

Without trolley: remove from /boot/extra then run removepkg. Maybe restart. Then, search the web for a new version, download it, get it on your unRAID box, install it, and remember to put it in /boot/extra for next time. Woof.

With trolley, it's just `trolley update openssl`.

### You need to install architecture specific versions

If you need a 64-bit package, go through the tedious install process, but be sure to get the x86_64 version and not the i*86 version. Oops, got the wrong one? Do over.

Trolley matches your arch automatically: `trolley install openssl`.

### You're a developer and you want to use trolley to manage your plugin's dependencies

If you're building a package with boiler, trolley is included automatically. If you're doing your own thing, add this to your code:

    [[ `command -v trolley` == "" ]] && wget -qO- --no-check-certificate http://git.io/8GviJQ | sh -

And specify versions (bash assumed):

    trolley install openssl "~> 1.0.1"
    trolley install glibc   "> 2.15"
    ...

## Usage

    root@Tower:~# trolley
    Commands:
      trolley help [COMMAND]          # Describe available commands or one specific command
      trolley info NAME [VERSION]     # Show package details
      trolley install NAME [VERSION]  # Install a new package
      trolley list [NAME]             # List installed packages
      trolley remove NAME             # Remove a package
      trolley search [NAME]           # Searches for matching packages
      trolley version                 # Show Trolley version

Tips

* If you do not want a package to be installed on reboot, remove it from `/boot/extra`.
* Trolley is optimistic about versions. It will always pick the newest, best match.
* If you do not specify a package version on install, the newest available package will be used.

## Examples

### Searching

Partial matches are supported.

    root@Tower:~# trolley search open
    openexr                openldap-client        openobex               openssh
    openssl                openssl-solibs         openvpn                xf86-video-openchrome
    open-cobol

### Listing installed

List everything

    root@Tower:~# trolley list
    aaa_base          14.1
    aaa_elflibs       14.1
    acl               2.2.51
    acpid             2.0.19
    apmd              3.2.2
    at                3.1.12
    ...

Filter the list with packages containing "tr"

    root@Tower:~# trolley list tr
    attr     2.4.46
    tree     1.6.0
    trolley  0.2.0_pre3

### Get info on a package

    root@Tower:~# trolley info openssl
    Name      openssl
    Summary   openssl (Secure Sockets Layer toolkit)
    Versions  0.9.8n, 0.9.8r, 0.9.8y, 1.0.1c, 1.0.1e, 1.0.1f

Get info on a specific version

    root@Tower:~# trolley info openssl 1.0.1e
    Name       openssl
    Summary    openssl (Secure Sockets Layer toolkit)
    Version    1.0.1e
    Arch       x86_64
    Build      1
    Size       12974080 (2912256 compressed)
    Slackware  14.1
    Patch      no

### Install a package

    root@Tower:~# trolley install openssl
    => Downloading openssl (1.0.1f)
    => Installing
    => Installed

## Spec

### Version constraints

The following version constraints are supported:

* >
* <
* =
* >=
* <=
* ~>

### Package matching

Trolley is **optimistic** when picking versions. It will always pick the newest available **except** when a package version isn't specified (`trolley install openssl`).

In this case, the most optimistic version available *for your Slackware version* will be used.

Example: if you're on Slackware 13.1 and you do `trolley install openssl`, 0.9.8y will be used.

You can override this behavior by specifying a version, or a constraint (eg, ">0").

### Architectures

32 and 64-bit architectures are automatically supported. Package matching rules apply in addition to matching the host OS arch.

### URLS

Trolley can install official packages by name. It also supports installing via url, if the package is a 3rd party Slackware package (the name will formatted NAME-VERSION-ARCH-BUILD.t*z).

## License

MIT. See LICENSE.txt for details.

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/nicinabox/trolley/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

