# sshping
Simple utility to ping servers that are only defined in your ~/.ssh/config file

Why? Because you can't just run ping against a host that cannot be resolved
thru standard means when it is ONLY specified in your ~/.ssh/config file ;)

I got tired of taking the ip out of the Hostname declaration...

## Usage

Very simple (although it will be simpler later, this is the first readme!):

    sudo python3 sshping.py some_target

"some_target" needs to be a Host definition in your .ssh/config - It may have a Hostname declaration,
but if that's not the case, it will just ping the some_target, assumming it can be resolved.



