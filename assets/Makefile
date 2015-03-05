
FOUNDATION_VERSION=5.5.1

.PHONY: clean

css/foundation.css: foundation.zip
	unzip -d foundation -o foundation.zip
	rm -r foundation/img
	rm foundation/humans.txt foundation/index.html foundation/robots.txt

foundation.zip:
	wget -O foundation.zip http://foundation.zurb.com/cdn/releases/foundation-$(FOUNDATION_VERSION).zip

clean:
	rm foundation.zip
