

raw_text = """
1
1These are the sayings of the great congregator, the son of David, the king of IsraEl in JeruSalem.

2The Great Congregator said:

‘All is foolishness and waste,
Foolishness and waste… All that’s done is in vain.’
3‘What value does man gain from the things he’s done,
And the things he’s worked hard for under the sun?

4‘For, one generation passes away,
And then another arrives…
Yet, the earth remains throughout the ages.

5‘The sun keeps on rising and setting
As it draws to it’s place,
6And the winds blow in from the south,
As they move north in a circle…
Then they go back and come ‘round again.

7‘Even though all the rivers flow into the sea,
The sea doesn’t become filled.
For, to the places from which they all came,
They return and flow back again.

8‘So, no man can speak all the words he might say,
And his eyes can’t be filled with all he can see,
Nor can his ears handle all that they hear.

9‘What’s this thing that [just] happened?
The same thing will happen again!
What’s this thing being done?
The same will be done in the future…
For there’s nothing that’s new under the sun!

10‘Who can say, Look, here’s something new?
For the same thing has happened for ages
To those who have lived before us.
11But the things that they did were forgotten,
And those who are born in the future
Won’t remember the things that we’re doing now.'

12The great congregator is the king over all of IsraEl from JeruSalem.

13‘So I set my heart to survey and inquire
About all that has happened under the sky.
God gave me this to distract me from bad,
And to lead sons of men back to Him.

14‘I’ve seen all that’s done under the sun,
And I find it to be a waste of [good] breath.
15For, things that go wrong are never made right,
And there’s too much that’s wrong to be counted.

16‘Once I spoke in my heart and I said:

Look how great I’ve become!
For, I’ve been given more wisdom
Than all who have lived before me!

‘So, I set my heart to learn wisdom and knowledge;
17And wisdom and knowledge, my heart then beheld,
As well as higher learning and proverbs.

‘So, it became the resolve of my spirit
18To gain an abundance of wisdom,
Along with vast volumes of knowledge.
But, those who gain knowledge also gain pain.’
"""

stopwords = """
i
me
my
myself
we
our
ours
ourselves
you
your
yours
yourself
yourselves
he
him
his
himself
she
her
hers
herself
it
its
itself
they
them
their
theirs
themselves
what
which
who
whom
this
that
these
those
am
is
are
was
were
be
been
being
have
has
had
having
do
does
did
doing
a
an
the
and
but
if
or
because
as
until
while
of
at
by
for
with
about
against
between
into
through
during
before
after
above
below
to
from
up
down
in
out
on
off
over
under
again
further
then
once
here
there
when
where
why
how
all
any
both
each
few
more
most
other
some
such
no
nor
not
only
own
same
so
than
too
very
s
t
can
will
just
don
should
now
things
thing
done
thats
that
ive
has
go
yet
wont
us
though
throughout
one
heres
doesnt
cant
"""

# sanitized = raw_text.replace('\r', '').replace('\n', '')   # not sure

scrubbed = ''
# sanitized_list = []
word_freq_dict = {}
counter = 0

for char in raw_text:
    if char.isalpha() or char == ' ' or char == '\n' or char == '\r':
        scrubbed += char.lower()

scrubbed_text_list = sorted(scrubbed.split())
stopwords_list = sorted(stopwords.split())

super_scrubbed_text_list = scrubbed_text_list[:]

for word in scrubbed_text_list:  # remove stopwords
    if word in stopwords_list:
        super_scrubbed_text_list.remove(word)

for word in super_scrubbed_text_list:
    if word not in word_freq_dict.keys():
        word_freq_dict[word] = 0
    word_freq_dict[word] += 1


print(scrubbed_text_list)
print(stopwords_list)
print(super_scrubbed_text_list)
print(word_freq_dict)
print(dict(sorted(word_freq_dict.items(), key=lambda item: item[1])))


# cloud = wordcloud.WordCloud()
# cloud.generate_from_frequencies(frequencies)
# cloud.to_file("myfile.jpg")
#



# filename = input('Enter a file name: ')
# contents = open(filename)
# for line in contents:
#     print(line.upper().rstrip())
