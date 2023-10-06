UDEVPREFIX = /etc/udev

INSTALLDATA = /usr/bin/install -c -m 644


install: all
	$(INSTALLDATA) 19-footswitch.rules $(DESTDIR)$(UDEVPREFIX)/rules.d

uninstall:
	rm -f $(DESTDIR)$(UDEVPREFIX)/rules.d/19-footswitch.rules
