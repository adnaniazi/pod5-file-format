"""
Testing Pod5Writer
"""
import lib_pod5 as p5b
import pytest

import pod5 as p5


class TestPod5Writer:
    """Test the Pod5Writer from a pod5 file"""

    def test_writer_fixture(self, writer: p5.Writer) -> None:
        """Basic assertions on the writer fixture"""
        assert isinstance(writer, p5.Writer)
        assert isinstance(writer._writer, p5b.FileWriter)

    @pytest.mark.parametrize("random_read", [1, 2, 3, 4], indirect=True)
    def test_writer_random_reads(self, writer: p5.Writer, random_read: p5.Read) -> None:
        """Write some random single reads to a writer"""

        writer.add_read(random_read)

    @pytest.mark.parametrize("random_read_pre_compressed", [1], indirect=True)
    def test_writer_random_reads_compressed(
        self, writer: p5.Writer, random_read_pre_compressed: p5.Read
    ) -> None:
        """Write some random single reads to a writer which are pre-compressed"""
        writer.add_read(random_read_pre_compressed)

    @pytest.mark.parametrize("random_read", [1, 2, 3, 4], indirect=True)
    def test_writer_random_reads_deprecated(
        self, writer: p5.Writer, random_read: p5.Read
    ) -> None:
        """Write some random single reads to a writer"""
        with pytest.deprecated_call():
            writer.add_read_object(random_read)

    @pytest.mark.parametrize("random_read_pre_compressed", [1], indirect=True)
    def test_writer_random_reads_compressed_deprecated(
        self, writer: p5.Writer, random_read_pre_compressed: p5.CompressedRead
    ) -> None:
        """Write some random single reads to a writer which are pre-compressed"""
        with pytest.deprecated_call():
            writer.add_read_object(random_read_pre_compressed)
