Decode a various fields related to EMV contact chip, paypass and paywave.

Deployed on Google App Engine [here](http://tvr-decoder.appspot.com).

Code now hosted on [github](https://github.com/binaryfoo/emv-bertlv).

Available as a library in [Maven Central](https://repo1.maven.org/maven2/io/github/binaryfoo/emv-bertlv/)

Available as an executable [jar file](https://repository.sonatype.org/service/local/artifact/maven/redirect?r=central-proxy&g=io.github.binaryfoo&a=emv-bertlv&c=shaded&v=LATEST). Eg:

<pre>
java -jar tvr-cmdline-1.0-alpha.jar<br>
Usage Main <decode-type> <value> [<tag-set>]<br>
<decode-type> is one of<br>
95: Terminal Verification Results<br>
9B: Transaction Status Indicator<br>
82: Application Interchange Profile<br>
8E: Cardholder Verification Method List<br>
9F34: Cardholder Verification Results<br>
9F6C: Card transaction qualifiers<br>
9F66: Terminal transaction qualifiers<br>
dol: Data Object List<br>
filled-dol: Data Object List<br>
constructed: Constructed TLV data<br>
apdu-sequence: Sequence of Command/Reply APDUs<br>
<value> is the hex string or '-' for standard input<br>
<tag-set> is one of [EMV, qVSDC, MSD] defaults to EMV<br>
</pre>