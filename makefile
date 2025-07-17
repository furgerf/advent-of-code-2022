DAY=
YEAR=2022

.PHONY: prepare-day

prepare-day:
ifndef DAY
	$(error Must specify DAY)
endif
	@if [ ! -f .aoc-session-cookie ]; then echo "Write AoC session cookie to '.aoc-session-cookie'"; false; fi
	@D=$$(printf "%02d" "$(DAY)") && \
		COOKIE=$$(cat .aoc-session-cookie) && \
		if [ -d "day_$$D" ]; then echo "Day $$D exists already!"; false; fi && \
		mkdir -p "day_$$D" && \
		cp day_template.py "day_$$D/day_$$D.py" && \
		sed -i "s/XXX/$$D/g" "day_$$D/day_$$D.py" && \
		http "https://adventofcode.com/$(YEAR)/day/$(DAY)/input" Cookie:session=$$COOKIE > "day_$$D"/input && \
		git add "day_$$D" && \
		echo "Prepared day $$D" && \
		echo "Number of input lines: $$(wc -l "day_$$D/input" | cut -d' ' -f 1)" && \
		head "day_$$D/input"
