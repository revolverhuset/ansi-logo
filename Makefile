OUT=20-logo

print:
	./pistol-logo.py

${OUT}: pistol-logo.py
	echo '#!/bin/bash' > ${OUT}
	echo 'cat <<EOF' >> ${OUT}
	./pistol-logo.py >> ${OUT}
	echo 'EOF' >> ${OUT}
	chmod a+x ${OUT}

deploy: ${OUT}
	scp ${OUT} revolverhuset.no:.
