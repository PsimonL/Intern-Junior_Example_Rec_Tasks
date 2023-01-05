import DuplicatesPac.Duplicates;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class UnitTests {
    @Test
    void InputExampleValues() {
        var testObj = new Duplicates();
        List<Integer> test_list;
        List<Integer> expected_list;

        test_list = Arrays.asList(-13, 6, 1, 1, 1, 1, 4, -4, 12, -4, 1, 5, 7, -2, 5);
        expected_list = Arrays.asList(-4, 5);
        assertEquals(testObj.findDuplicates(test_list, 2), expected_list);

        test_list = Arrays.asList(1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3);
        expected_list = Arrays.asList(1, 3);
        assertEquals(testObj.findDuplicates(test_list, 5), expected_list);

        test_list = Arrays.asList(0, 1, 7, 7, -1, -21, -4, 2, -4, 14, 76, 3, -5, 5);
        expected_list = Arrays.asList(-21, -5, -1, 0, 1, 2, 3, 5, 14, 76);
        assertEquals(testObj.findDuplicates(test_list, 1), expected_list);

        test_list = Arrays.asList(-1, 0, 1, 1, 1, 2, 3);
        expected_list = Arrays.asList();
        assertEquals(testObj.findDuplicates(test_list, 100), expected_list);
    }
}