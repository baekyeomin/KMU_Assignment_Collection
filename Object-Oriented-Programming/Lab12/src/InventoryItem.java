// ***********************************************************************
// InventoryItem.java
//
// Represents an item in the inventory.
// ***********************************************************************
import java.text.DecimalFormat;
public class InventoryItem
{
	private String name;
	private int units; // number of available units of this item
	private float price; // price per unit of this item
	private DecimalFormat fmt;
// ----------------------------------------------------------------
// Sets up this item with the specified information.
// ----------------------------------------------------------------
	public InventoryItem (String itemName, int numUnits, float cost)
	{
		name = itemName;
		units = numUnits;
		price = cost;
		fmt = new DecimalFormat ("0.##");
	}
// ----------------------------------------------------------------
// Returns information about this item as a string
// ----------------------------------------------------------------
	public String toString()
	{
		return name + ":\t" + units + " at " + price + " = " +
				fmt.format ((units * price));
	}
// ---------------------------------------------------------------
// Returns the name of the item.
// ---------------------------------------------------------------
	public String getName()
	{
		return name;
	}
// ---------------------------------------------------------------
// Returns the number of available units of the item
// ---------------------------------------------------------------
	public int getUnits ()
	{
		return units;
	}
// ---------------------------------------------------------------
// Returns the price of the item.
// ---------------------------------------------------------------
	public float getPrice()
	{
		return price;
	}
// ---------------------------------------------------------------
// Adds the specified number to the available units
// ---------------------------------------------------------------
	public void restock (int addedUnits)
	{
		units += addedUnits;
	}
}